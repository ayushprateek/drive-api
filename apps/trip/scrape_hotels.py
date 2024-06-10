import json
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import re
import random

from apps.trip import helper
from selenium import webdriver
from apps.trip.models import City, Hotel
from common.cloud_service import process_hotel_images, upload_file_to_aws_s3
from common.constants import Constant, common_descriptions


class ScrapeHotels:
    """
    A class to scrape hotel details from given URLs.

    Attributes:
    ----------
    city : str, optional
        Name of the city the hotel is located in.
    category : str, optional
        Category or type of the hotel (e.g. Luxury, Budget).
    url : str
        URL of the hotel website to be scraped.
    """

    def __init__(self, url, city=None, category=None):
        """Initialize the ScrapeHotels with a given URL and optional city and category."""
        self.city = city
        self.category = category
        self.url = url

    @staticmethod
    def find_key(data, target_key):
        """Recursively search for a key in a nested dictionary or list."""
        if isinstance(data, dict):
            if target_key in data:
                return data[target_key]
            for key, value in data.items():
                result = ScrapeHotels.find_key(value, target_key)
                if result:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = ScrapeHotels.find_key(item, target_key)
                if result:
                    return result
        return None

    def scrape_from_choice_hotels(self, html_content):
        """Extract hotel details from Choice hotel's website HTML content."""
        script_tag = html_content.find_all('script', type="application/ld+json")

        # Parse the JSON data
        ld_json_data = [json.loads(i.string) for i in script_tag if i]

        amenities = ScrapeHotels.find_key(ld_json_data, 'amenityFeature')
        source_urls = [source['srcset'] for source in html_content.find_all('source') if 'srcset' in source.attrs]
        images = [f"https://www.choicehotels.com{i}" for i in source_urls]

        hotel_rating = ScrapeHotels.find_key(ld_json_data, 'aggregateRating')
        hotel_reviews = {
            "text": f"{hotel_rating.get('ratingValue')} / 5",
            "image": None,
            "rating_data": {
                "rating": hotel_rating.get('ratingValue'),
                "rating_count": hotel_rating.get('ratingCount'),
                "best_rating": hotel_rating.get('bestRating'),
                "review_count": hotel_rating.get('reviewCount')
            }
        }
        hotel_info = next((i for i in ld_json_data if i.get("@type") == 'Hotel'), {})
        hotel_name = hotel_info.get("name")
        description = hotel_info.get("description")
        address = hotel_info.get("address")
        contact_us = {"phone": hotel_info.get("telephone")}

        items = html_content.select("#hotel-attractions .destination-list li")
        facility_overview = [{"name": item.select_one(".name").get_text(strip=True),
                              "distance": item.select_one(".distance").get_text(strip=True)} for item in items]

        info_items = html_content.select(".property-info ul li")

        info_dict = {
            item.h6.get_text().strip():
                item.div.get_text(strip=True) + (" ".join(
                    ["{}{}".format(
                        span.select_one('.text-semibold').get_text() if span.select_one('.text-semisolid') else '',
                        span.contents[-1].get_text()) for span
                        in
                        item.select('.list-data div.block')]) if item.select('.list-data') else "")
            for item in info_items
        }

        info_dict["Hotel Alerts"] = [p.get_text() for p in html_content.select(".hotel-policies p")]

        check_in_info = {"checkin_time": info_dict.get("Check-In"),
                         "checkout_time": info_dict.get("Check-Out")}

        meta_data = {"scraped_from": self.url, "website_data": ld_json_data, "scrape_data": f'{html_content}'}

        scrapped_data = {
            "name": hotel_name,
            "city_name": address.get("addressLocality"),
            "description": description,
            "contact_info": contact_us,
            "check_in_data": check_in_info,
            "address": address,
            "latitude": None,
            "longitude": None,
            "hotel_reviews": hotel_reviews,
            "amenities": {"amenities": amenities},
            "service_amenities": {},
            "facility_overview": facility_overview,
            "hotel_policy": {},
            "meta_data": meta_data,
            "cover_image": None,
            "images": images
        }

        return scrapped_data

    def scrape_from_hilton_site(self, html_content):
        """Extract hotel details from Hilton's website HTML content."""
        # Extract images with the specified class
        img_tags = html_content.select(".snap-center.rounded.hidden img")
        hotel_images = [img['src'] for img in img_tags]

        # Extract hotel review details
        img_tag = html_content.find('img', class_="relative -left-4 mb-2 block w-44 sm:left-0 md:w-40")
        hotel_reviews = {}
        if img_tag:
            hotel_reviews = {
                "text": img_tag['alt'],
                "image": img_tag['src']
            }
        # Extract JSON-LD data for structured hotel details
        script_tag = html_content.find('script', type="application/ld+json")
        json_data = json.loads(script_tag.string) if script_tag else {}

        # Organize hotel details into respective sections
        all_json_data = [json.loads(script.string) for script in
                         html_content.find_all('script', type="application/json")]
        amenities = self.find_key(all_json_data, 'amenities')
        facility_overview = self.find_key(all_json_data, 'facilityOverview')
        policy = self.find_key(all_json_data, 'policy')
        service_amenities = self.find_key(all_json_data, 'serviceAmenities')

        # Collate all details into a single dictionary
        meta_data = {"scraped_from": self.url, "website_data": all_json_data}

        scrapped_data = {
            "name": json_data.get("name"),
            "city_name": json_data.get("address", {}).get("addressLocality"),
            "description": json_data.get("description"),
            "contact_info": {"phone": json_data.get("telephone")},
            "check_in_data": {
                "checkin_time": json_data.get("checkinTime"),
                "checkout_time": json_data.get("checkoutTime")
            },
            "address": json_data.get("address"),
            "latitude": json_data.get("geo", {}).get("latitude"),
            "longitude": json_data.get("geo", {}).get("longitude"),
            "hotel_reviews": hotel_reviews,
            "amenities": {"amenities": amenities},
            "service_amenities": {"service_amenities": service_amenities},
            "facility_overview": facility_overview,
            "hotel_policy": policy,
            "meta_data": meta_data,
            "cover_image": None,
            "images": hotel_images
        }
        # Hotel.create_instance(scrapped_data)
        return scrapped_data

    def scrape_from_marriott_site(self, html_content):
        """Extract hotel details from Marriott's website HTML content."""
        # Extract contents with the specified class
        scrapped_data = {}

        content_body = html_content.find(class_="main-content")
        extra_info = content_body.find(class_="getting-here-panel")
        check_in_data = content_body.find(class_="col-12 col-xl-6 pl-0 pr-0 pr-xl-4")
        check_in_time = content_body.find(class_="hotel-info-container d-flex flex-column container")
        content = content_body.find(class_="d-flex flex-column justify-content-center col-12 col-xl-10")

        # Extract contents
        if content:
            scrapped_data.update({"description": content.find('p').text.replace("\n", "")})

        # Extract title 
        if content:
            title = content.find('h2')
        else:
            content = content_body.find(class_="d-flex flex-column justify-content-center col-12 col-xl-10 py-xl-3")
            title = content.find('h2')
        if title:
            scrapped_data.update({"name": title.text.replace("\n", "")})

        # Extract contact information
        contact_info = html_content.find(class_="phoneNumber t-font-s uppercase m-0 pb-2")
        if contact_info:
            scrapped_data.update({"contact_info": {"contact_info": contact_info.text}})

        # Extract location elements    
        location_content = content_body.find(class_="dynamic-footer__social-media col-12 col-xl-6 px-0 px-xl-2")
        location_elements = html_content.find(class_='dynamic-footer__social-media col-12 col-xl-6 px-0 px-xl-2')

        if location_elements:
            address_element = location_content.find_all("p")
            address = [p.text for p in address_element]
            scrapped_data.update({"address": {"address": address}})
            scrapped_data.update({"latitude": None, "longitude": None, "city_name": None})

        # Extract the image URLs from theaddress.get("addressLocality") style attribute
        image_elements = html_content.find_all('div', class_='bg-image')
        image_urls = [element['style'].split("url('")[1].split("')")[0] for element in image_elements]
        if image_urls:
            scrapped_data.update({"images": image_urls, "cover_image": image_urls})
        if extra_info:
            cleaned_data = '\n'.join(line.strip() for line in extra_info.get_text().splitlines() if line.strip())
            scrapped_data.update({"meta_data": {"getting_here": cleaned_data.replace("\n", ", ")}})

        # amenities-container d-flex flex-column container
        amenities = content_body.find(class_="amenities-container d-flex flex-column container")
        if amenities:
            cleaned_data = '\n'.join(line.strip() for line in amenities.get_text().splitlines() if line.strip())
            scrapped_data.update({"amenities": {"amenities": cleaned_data.replace("\n", ", ")}})

        # Extract Check In Data
        if check_in_data:
            cleaned_data = '\n'.join(line.strip() for line in check_in_time.get_text().splitlines() if line.strip())
            scrapped_data.update({"check_in_data":
                                      {"check_in_data": check_in_data.find(
                                          class_="accordion-content py-3").get_text().replace("\n", " "),
                                       "check_in_timings": cleaned_data.replace("\n", ", ")}})

        return scrapped_data

    def scrape_from_wyndham_hotels(self, html_content):
        """
        Extract hotel details from Wyndham Hotels website HTML content.

        Args:
        - html_content (bs4.BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

        Returns:
        - dict: A dictionary containing the extracted hotel information.
        """
        # Extract JSON data from script tags
        script_tags = html_content.find_all('script', type="application/ld+json")
        ld_json_data = [json.loads(tag.string) for tag in script_tags if tag.string]

        # Extract amenities from the HTML content
        amenities_list = html_content.select(".hotel-amenities li")
        amenities = [item.text.strip() for item in amenities_list]

        description_tag = html_content.find('meta', attrs={'name': 'description'})

        # Extract the content attribute
        description = description_tag['content'] if description_tag else None

        # Extract hotel information from the JSON data
        hotel_info = next((item for item in ld_json_data if item.get("@type") == 'Hotel'), {})
        hotel_name = hotel_info.get("name")
        cover_image = hotel_info.get("image")
        latitude = hotel_info.get("geo", {}).get("latitude")
        longitude = hotel_info.get("geo", {}).get("longitude")
        contact_info = {"phone": hotel_info.get("telephone")}
        address = hotel_info.get("address")

        # Meta data for debugging or further use
        meta_data = {
            "scraped_from": self.url,
            "website_data": ld_json_data,
            "scraped_data": str(html_content)
        }
        image_urls = []
        image_containers = html_content.find_all('div', class_='pll-image-container')
        for container in image_containers:
            # Find the 'img' tag inside each 'div' with class 'pll-image-container'
            img_tag = container.find('img')

            # Extract the 'src' attribute from the 'img' tag
            if img_tag and 'src' in img_tag.attrs:
                image_url = img_tag['src']
                image_urls.append(image_url)

        images = []

        if image_urls:
            images = [f"https://{Constant.WYNDHAM_HOTELS}/{image}" for image in image_urls if image.startswith('/')]

        if not images:
            if cover_image and cover_image.startswith('https'):
                images = [cover_image]
            if cover_image and cover_image.startswith('/'):
                images = [f"https://{Constant.WYNDHAM_HOTELS}/{cover_image}"]


        # Collate all details into a single dictionary
        scrapped_data = {
            "name": hotel_name,
            "city_name": address.get("addressLocality"),
            "description": description,
            "contact_info": contact_info,
            "check_in_data": {},
            "address": address,
            "latitude": latitude,
            "longitude": longitude,
            "hotel_reviews": {},
            "amenities": {"amenities": amenities},
            "service_amenities": {"service_amenities": []},
            "facility_overview": {},
            "hotel_policy": {},
            "meta_data": meta_data,
            "cover_image": cover_image,
            "images": images
        }

        return scrapped_data

    def scrape_from_ihg_hotels(self, html_content):
        """
        Extract hotel details from IHG Hotels website HTML content.

        Args:
        - html_content (bs4.BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

        Returns:
        - dict: A dictionary containing the extracted hotel information.
        """
        # Extract JSON data from script tags
        script_tags = html_content.find_all('script', type="application/ld+json")
        ld_json_data = [json.loads(tag.string) for tag in script_tags if tag.string]

        # Extract amenities from the HTML content
        amenity_divs = html_content.select(".vx-highlight-item")

        amenities = []

        # Extract the amenity information and append to the list
        for div in amenity_divs:
            name = div.find("div", class_="amenity-title").text.strip()
            description = div.find("div", class_="amenity-title").text.strip()

            amenity_dict = {
                "name": name,
                "description": description
            }
            amenities.append(amenity_dict)

        # Extract hotel information from the JSON data
        hotel_rating = ScrapeHotels.find_key(ld_json_data, 'aggregateRating')
        hotel_reviews = {
            "text": f"{hotel_rating.get('ratingValue')} / 5",
            "image": None,
            "rating_data": {
                "rating": hotel_rating.get('ratingValue'),
                "rating_count": hotel_rating.get('ratingCount'),
                "best_rating": hotel_rating.get('bestRating'),
                "review_count": hotel_rating.get('reviewCount')
            }
        }
        hotel_info = next((item for item in ld_json_data if item.get("@type") == 'Hotel'), {})
        hotel_name = hotel_info.get("name")
        description = hotel_info.get("description")
        cover_image = hotel_info.get("image")
        latitude = hotel_info.get("geo", {}).get("latitude")
        longitude = hotel_info.get("geo", {}).get("longitude")
        contact_info = {"phone": hotel_info.get("telephone")}
        address = hotel_info.get("address")

        # Meta data for debugging or further use
        meta_data = {
            "scraped_from": self.url,
            "website_data": ld_json_data,
            "scraped_data": str(html_content)
        }

        # Collate all details into a single dictionary
        scrapped_data = {
            "name": hotel_name,
            "city_name": address.get("addressLocality"),
            "description": description,
            "contact_info": contact_info,
            "check_in_data": {},
            "address": address,
            "latitude": latitude,
            "longitude": longitude,
            "hotel_reviews": hotel_reviews,
            "amenities": {"amenities": amenities},
            "service_amenities": {"service_amenities": []},
            "facility_overview": {},
            "hotel_policy": {},
            "meta_data": meta_data,
            "cover_image": cover_image,
            "images": []
        }

        return scrapped_data

    def scrape_from_offthechart_site(self, html_content):
        """
        Extract hotel details from Off The Chart Hotels website HTML content.

        Args:
        - html_content (bs4.BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

        Returns:
        - dict: A dictionary containing the extracted hotel information.
        """

        scrapped_data = {}
        meta_data = {"scraped_from": self.url}
        # Find the div element with the background-image property
        div_element = html_content.find_element(By.CLASS_NAME, "wsite-header-section")

        # Extract the background-image property value
        background_image_style = div_element.get_attribute("style")
        if background_image_style:
            # Extract the image URL from the style attribute
            cover_image = self.url.replace("/index.html", "") + background_image_style.split('url("', 1)[1].split('")')[
                0]
            scrapped_data.update({"cover_image": cover_image})

        # Find the paragraph element containing the phone number and email
        paragraph_element = html_content.find_element(By.CLASS_NAME, "paragraph")
        if paragraph_element:
            # Extract the text from the paragraph
            paragraph_text = paragraph_element.text
            # Split the text to extract the phone number and email

            # Extract phone number using regular expression
            phone_pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')
            phone_match = phone_pattern.search(paragraph_text)
            phone_number = phone_match.group() if phone_match else None

            # Extract email address using regular expression
            email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
            email_match = email_pattern.search(paragraph_text)
            email = email_match.group() if email_match else None
            scrapped_data.update({"contact_info": {"email": email,
                                                   "phone_number": phone_number}})

        # Find all the anchor elements that link to images
        image_links = html_content.find_elements(By.CSS_SELECTOR, ".galleryImage")

        # Extract the image URLs
        image_list = []
        if image_links:
            for link in image_links:
                image_list.append(link.get_attribute("src"))
        scrapped_data.update({"images": image_list})

        address_element = html_content.find_element(By.CLASS_NAME, "footer")
        if address_element:
            address = address_element.find_element(By.CLASS_NAME, "paragraph").text
            scrapped_data.update({"address": {"address": address},
                                  "name": "Off the Charts Inn & Out Island Resort",
                                  "city_name": "St. James City"})
        scrapped_data.update({"meta_data": meta_data})
        # Return the scrapped data 
        return scrapped_data

    def scrape_from_dunnelon_site(self, html_content):
        """
        Extract hotel details from Dunnel On Motels  website HTML content.

        Args:
        - html_content (bs4.BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

        Returns:
        - dict: A dictionary containing the extracted hotel information.
        """

        scrapped_data = {}

        # Meta data
        meta_data = {"scrapped_from": self.url}

        # Extract the description
        content_element = html_content.find_element(By.CLASS_NAME, "Normal_text")
        if content_element:
            scrapped_data.update({"description": content_element.text})

        # Find the title element
        css_selector = ".xr_tc.Normal_text"
        title_element = html_content.find_element(By.CSS_SELECTOR, css_selector)
        if title_element:
            scrapped_data.update({"name": title_element.text})

        # Extract the background-image property value
        images = []
        image_element = html_content.find_element(By.CSS_SELECTOR,
                                                  "img.xr_ap[src*='index_htm_files/44.jpg']")
        if image_element:
            # Extract the src attribute (image URL)
            images.append(image_element.get_attribute("src"))

        # Extract the background-image property value
        class_name = "xr_rn_.xr_ap"
        image_element = html_content.find_element(By.CSS_SELECTOR, f"img.{class_name}")
        if image_element:
            # Extract the src attribute (image URL)
            images.append(image_element.get_attribute("src"))

        scrapped_data.update({"images": images,
                              "meta_data": meta_data,
                              "city_name": None,
                              "latitude": None,
                              "longitude": None})

        # Return the scrapped data
        return scrapped_data

    def scrape_from_groupon_site(self, html_content):
        """
        Extract hotel details from Groupon website HTML content.

        Args:
        - html_content (bs4.BeautifulSoup): A BeautifulSoup object containing the parsed HTML of the webpage.

        Returns:
        - dict: A dictionary containing the extracted hotel information.
        """
        # Extract final scrapped data
        scrapped_data = []

        hotel_html_contents = html_content.find_all(class_="cui-content")
        for item in hotel_html_contents:
            # Extract each hotel details 
            hotel_data = {}
            meta_data = {"scraped_from": self.url}
            # Extract each hotel html content
            details = item.find(class_="cui-udc-details")

            # Extract the hotel name
            if details.find(class_="cui-udc-subtitle one-line-truncate"):
                # Update the hotel name
                hotel_data.update({"name": details.find(
                    class_="cui-udc-subtitle one-line-truncate").get_text().replace('\n', '')})

                # Extract the hotel ratings
                if details.find(class_="cui-sr-only"):
                    meta_data.update({"ratings": details.find(class_="cui-sr-only").get_text()})

                # Extract the hotel discounted price
                if details.find(class_="cui-price-original c-txt-gray-dk"):
                    meta_data.update({"actual_price": details.find(
                        class_="cui-price-original c-txt-gray-dk").get_text()})

                # Extract the hotel discounted price
                if details.find(class_="cui-price-discount c-txt-price"):
                    meta_data.update({"discounted_price": details.find(
                        class_="cui-price-discount c-txt-price").get_text().replace('\xa0', ' ')})

                # Extract the hotel description
                if details.find(class_="cui-description"):
                    hotel_data.update({"description": details.find(class_="cui-description").get_text()})

                else:
                    # Update random description if not found in the html content
                    hotel_data.update({"description": random.choice(common_descriptions)})

                    # Extract city name from url
                city_name = self.url.split('/')[4]

                # Update latitude, longitude and city name
                hotel_data.update({"latitude": None, "longitude": None, "city_name": city_name})

                # Extract the hotel images
                image_tag = html_content.find('img', class_='cui-image')
                if image_tag:
                    images = []
                    image_element = image_tag['srcset']
                    for item in image_element.split(','):
                        original_image_url = item.replace('\n', '').replace(' ', '')
                        modified_url = ''.join([original_image_url[:-2] if original_image_url.endswith('1x')
                                                                           or original_image_url.endswith(
                            '2x') else original_image_url])
                        updated_modified_url = "https:" + modified_url
                        image_url, s3_key = upload_file_to_aws_s3(updated_modified_url)
                        if image_url and s3_key:
                            images.append(image_url)
                    # Update the hotel images
                    hotel_data.update({"image": images})
                # Append the hotel data to scrapped data
                hotel_data.update({"meta_data": meta_data})
                scrapped_data.append(hotel_data)
        return scrapped_data

    def scrape_from_bestwestern(self, html_content):
        scrapped_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract main data
        main_data = html_content.find(class_="hotelRoomsContainer row fullWidthVariation")

        # Extract title from page
        title = main_data.title.text.strip()

        # Extract description from page
        description = re.sub('\s+', ' ', main_data.text)

        # Extract image_elements from page
        image_elements = main_data.find_all(class_='hotelImage')

        # Extract image URLs from the style attribute
        images = [element['style'].split('url(')[-1].rstrip(');') for element in image_elements]

        scrapped_data.update({"images":images, "name":title,
                              "description":description, "meta_data":meta_data, 
                              "latitude":None, "longitude":None})

        return scrapped_data

    def scrape_data(self):
        """Main method to orchestrate the scraping process."""
        domain = self.url.split('/')[2]
        # If URL has already been scraped, we avoid scraping it again
        if Hotel.filter_instance({"meta_data__scraped_from": self.url}):
            return None
        if domain == Constant.MARRIOT_HOTELS:
            response = requests.get(self.url)
            if response.status_code == 200:
                html_content = BeautifulSoup(response.text, "html.parser")
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/93.0.4577.63 Safari/537.36")
            driver = webdriver.Chrome(options=options)
            driver.get(self.url)
            driver.implicitly_wait(10)
            if domain in [Constant.OFFTHECHART, Constant.DUNNELON_MOTELS]:
                html_content = driver
            else:
                # Convert page source to BeautifulSoup object for parsing
                html_content = BeautifulSoup(driver.page_source, 'html.parser')
        scrape_data = {}
        scraper_function_map = {
            Constant.CHOICE_HOTELS: self.scrape_from_choice_hotels,
            Constant.HILTON_SITE: self.scrape_from_hilton_site,
            Constant.WYNDHAM_HOTELS: self.scrape_from_wyndham_hotels,
            Constant.IHG_HOTELS: self.scrape_from_ihg_hotels,
            Constant.MARRIOT_HOTELS: self.scrape_from_marriott_site,
            Constant.OFFTHECHART: self.scrape_from_offthechart_site,
            Constant.DUNNELON_MOTELS: self.scrape_from_dunnelon_site,
            Constant.GROUPON_SITE: self.scrape_from_groupon_site,
            Constant.BESTWESTERN: self.scrape_from_bestwestern
        }
        # Calling the appropriate scraping function based on the domain.
        if domain in scraper_function_map:
            scrape_data = scraper_function_map[domain](html_content)
        if domain != Constant.MARRIOT_HOTELS:
            driver.close()

        if scrape_data:
            if isinstance(scrape_data, list):
                instances_to_insert = []

                # Loop each hotel and fetch address
                for item in scrape_data:
                    city_object = None
                    if item["city_name"]:
                        city_object = City.get_instance_or_none({"name": item["city_name"]})
                        if not city_object:
                            city_object = City.create_instance({"name": item["city_name"]})
                    data = {
                        'name': item['name'],
                        'description': item.get('description', ''),
                        'images': item.get('images', []),
                        'meta_data': item.get('meta_data', {}),
                        'city': city_object
                    }
                    geo_dt, api_data = helper.get_geo_data(item.get('name'))
                    if not geo_dt:
                        geo_dt, api_data = helper.get_geo_data(item.get('city_name'))
                    data["meta_data"]["address"] = api_data
                    data['latitude'] = geo_dt.get("latitude")
                    data['longitude'] = geo_dt.get("longitude")

                    instance = Hotel(**data)
                    instances_to_insert.append(instance)

                # Bulk create hotel instances
                if instances_to_insert:
                    instances = Hotel.objects.bulk_create(instances_to_insert)
                    return instances
                else:
                    return []
            geo_dt, city_name = {}, scrape_data.pop("city_name")
            if scrape_data.get("latitude") is None or scrape_data.get("longitude") is None:
                geo_dt, api_data = helper.get_geo_data(scrape_data.get('name'))
                scrape_data["meta_data"]["address"] = api_data
                scrape_data['latitude'] = geo_dt.get("latitude")
                scrape_data['longitude'] = geo_dt.get("longitude")

            if city_name is None:
                if geo_dt:
                    city_name = geo_dt.get("city_name")
                else:
                    geo_dt, api_data = helper.get_geo_data(scrape_data.get('name'))
                    city_name = geo_dt.get("city_name")

            if city_name:
                city_object = City.get_instance_or_none({"name": city_name})
                if not city_object:
                    city_object = City.create_instance({"name": city_name})

                scrape_data['city_id'] = city_object.id if city_object else None

        hotel_obj = Hotel.get_instance_or_none({"name": scrape_data.get("name")})
        if hotel_obj:
            return scrape_data

        scrape_data["images"] = process_hotel_images(images=scrape_data["images"])
        Hotel.create_instance(scrape_data)
        return scrape_data
