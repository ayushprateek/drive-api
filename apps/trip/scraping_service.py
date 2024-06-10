import html
import json
import re

import requests
from bs4 import BeautifulSoup
from apps.trip import helper
from selenium import webdriver
from selenium.webdriver.common.by import By

from apps.trip.services.common import get_geo_code, get_geo_code_area
from apps.user.models import Media
from common.cloud_service import upload_file_to_aws_s3

from urllib.parse import urlparse, urlunparse

from common.constants import Constant
from drive_ai import settings


class Scrape:

    def __init__(self, city, category, url):
        self.city = city
        self.category = category
        self.url = url

    @staticmethod
    def find_domain(url):
        # Use regular expression to extract "DOMAIN6"
        match = re.search(r'CDNDOMAIN(\d+)', url)
        if match:
            cdn_domain = match.group(0)
            match = re.match(r"([a-zA-Z]+)(\d+)", cdn_domain)
            output_url = re.sub(r'CDNDOMAIN\d+', f"cdn{match.group(2)}.localdatacdn.com", url)
            return output_url
        else:
            return url

    @staticmethod
    def extract_json_from_script(script_content):
        """
        Extract a JSON object string from a script content based on a specific keyword.

        Given the content of a script, this method tries to find a JSON object that follows
        a specific keyword (e.g., 'partnerDetails:'). The method returns the extracted JSON
        string if successful or None if the JSON object isn't found or if there's a mismatch
        in the braces.

        Args:
            script_content (str): The content of the script from which to extract the JSON string.

        Returns:
            Optional[str]: The extracted JSON string if successful; otherwise, None.

        """
        # The keyword that precedes the JSON object in the script content.
        start_keyword = 'partnerDetails:'

        # Find the starting position of the JSON object by locating the keyword.
        start_index = script_content.find(start_keyword)
        if start_index == -1:
            return None
        start_index = script_content.find('{', start_index)

        end_index = start_index
        brace_balance = 0  # To keep track of the opening and closing braces.

        # Iterate through the script content to find the end of the JSON object.
        while end_index < len(script_content):
            if script_content[end_index] == '{':
                brace_balance += 1
            elif script_content[end_index] == '}':
                brace_balance -= 1

            # If the braces balance out, we've found the end of the JSON object.
            if brace_balance == 0:
                break

            end_index += 1

        # If braces don't balance out, the JSON string extraction failed.
        if brace_balance != 0:
            return None

        # Return the extracted JSON string.
        return script_content[start_index:end_index + 1]

    def scrape_data_from_restaurantji_site(self, html_content):
        """
        Extract restaurant details from the restaurantji website.

        This method fetches the restaurant details, such as name, address, latitude,
        longitude, and image from a given HTML content. Additionally, it makes
        a request to an S3 bucket to get the content of the city's HTML file and
        uses it to extract further details like the restaurant description.

        Args:
            html_content (BeautifulSoup): The HTML content to scrape.

        Returns:
            dict: A dictionary containing the scraped data including name, latitude, longitude,
                  description, image, and metadata about the restaurant.

        Raises:
            JSONDecodeError: If there's an error decoding the JSON content from the script tag.
        """
        # Extract the JSON content from the script tag on the page.
        script_tag = html_content.find('script', type="application/ld+json")
        scrape_data = {}
        meta_data = {}

        data = json.loads(script_tag.string)
        name = data.get("name")
        meta_data["address"] = data.get("address", {})
        meta_data["scraped_from"] = self.url
        latitude, longitude = data.get("address", {}).get("latitude"), data.get("address", {}).get("longitude")
        scrape_data.update({"name": name, "latitude": latitude, "longitude": longitude})

        # Construct the URL to get the content of the city's HTML file from S3.
        s3_url = (f"https://s3.amazonaws.com/{settings.AWS_BUCKET}/" +
                  f"site_data/{self.city.replace(' ', '-').lower()}.html")

        response = requests.get(s3_url)
        full_site_content = response.content

        soup = BeautifulSoup(full_site_content, 'html.parser')
        # Extract all restaurant listings on the page.
        restaurant_listings = soup.find_all(class_="strip grid")

        # Iterate through each restaurant listing to find the matching restaurant and its details.
        for item in restaurant_listings:
            rest_name = item.find(class_="read_more").get_text()
            if rest_name == name:
                scrape_data.update({"description": item.find('p').get_text()})
                image_element = item.find("img")
                if image_element:
                    image_url = image_element.get("data-src")
                    modified_image_url = Scrape.find_domain(image_url)
                    media_url, media_key = upload_file_to_aws_s3(modified_image_url)
                    if media_url and media_key:
                        scrape_data.update({"images": [media_url]})

        scrape_data["meta_data"] = meta_data
        return scrape_data

    def scrape_data_floridastateparks_site(self, html_content):
        """
        Extract relevant information from the Florida State Parks site's HTML content.

        This function processes the provided HTML content to retrieve details such as the park name,
        description, and associated image from the Florida State Parks website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, and image.
        """

        # Initializing data dictionary with meta information.
        meta_data = {"scraped_from": self.url}
        data = {"meta_data": meta_data, "latitude": None, "longitude": None}

        # Extract the main content body.
        content_body = html_content.find(class_="main")

        # Extract the park name/title.
        title = content_body.find(class_="hero__content")
        h1_element = title.find("h1", class_="hero__title")
        if h1_element:
            data["name"] = h1_element.text.strip()

        # Extract park description.
        description = content_body.find(class_="l-sidebar__main")
        if description:
            data["description"] = description.get_text().replace("\n", " ")

        # Extract and upload the associated image to AWS S3.
        image_element = content_body.find("img")
        if image_element:
            image_url = f"https://{Constant.FLORIDA_STATE_SITE}" + image_element.get("src")
            image_url, s3_key = upload_file_to_aws_s3(image_url)
            if image_url and s3_key:
                data["images"] = [image_url]

        return data

    def scrape_data_from_miami_beach_site(self, html_content):
        """
        Extract relevant information from the Miami Beach site HTML content.

        This function scrapes data such as geographic location, metadata, and media
        details from the provided HTML content. The scraped details are then structured
        and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing scraped details including name, description, geo-coordinates, and image information.

        Raises:
        - Exception: If there's an issue during JSON decoding.
        """

        try:
            # Extract meta data from script tags
            script_tag = html_content.find('script', type="application/ld+json")
            geo_dt = {}
            meta_data = {}
            if script_tag:
                data = json.loads(script_tag.string)
                meta_data["address"] = data.get("address", {})
                geo_dt = data.get("geo", {})
                meta_data["geo_data"] = geo_dt

            # Extracting entity name and description from meta tags
            entity_name = html_content.find('meta', {'property': 'og:title'})
            desc = html_content.find('meta', {'property': 'og:description'})

            name = entity_name.get("content").replace(' ', '-').lower() if entity_name else None
            description = desc.get("content") if desc else None

            # Parsing additional data from embedded scripts
            script_content = html_content.find('script', string=re.compile('partnerDetails:')).string
            data_str = Scrape.extract_json_from_script(script_content)
            entity_data = json.loads(data_str)
            meta_data["scrape_data"] = entity_data
            meta_data["scraped_from"] = self.url

            # Extracting primary image details
            image_data = entity_data.get("listingImages", [])
            image = image_data[0] if image_data else {}
            media = None
            if image:
                img_url = image.get("url")
                parsed = urlparse(img_url)
                if not parsed.scheme:
                    img_url = 'https://' + img_url.lstrip('/')
                image_url, s3_key = upload_file_to_aws_s3(img_url)
                if image_url and s3_key:
                    image_url = [image_url]

            # Extracting and cleaning up description content
            desc_content = entity_data.get("listingFacilityInformation", {}).get("meetingInformation", {}).get(
                "description")
            if desc_content:
                soup = BeautifulSoup(desc_content, 'html.parser')
                description = soup.get_text()
                description = html.unescape(description).replace('\n', ' ').replace('\xa0', ' ')

            # Structuring the final scrape data based on category
            scrape_data = {
                "name": name,
                "city_id": self.city,
                "latitude": geo_dt.get("latitude"),
                "longitude": geo_dt.get("longitude"),
                "description": description,
                "images": image_url,
                "meta_data": meta_data
            }
            return scrape_data

        except json.JSONDecodeError:
            raise Exception("Failed to Scrape Data from Miami beach site")

    def scrape_data_from_visitorlando_site(self, html_content):
        """
        Extract relevant information from the Visitorlando site's HTML content.

        This function processes the given HTML content to scrape details like
        title, description, and image from the Visitorlando website. The function then
        structures and returns these details in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing scraped details including name, description, and image information.

        """

        # Initialize a dictionary to store scraped data.
        data = {}
        meta_data = {"scraped_from": self.url}
        data["meta_data"] = meta_data

        # Extract main content block.
        content_body = html_content.find(class_="detail-top")

        # Extract title and description.
        title = content_body.find(class_="title-panel").get_text(strip=True)
        description = content_body.find(class_="content-panel desktop").get_text(strip=True)

        # Attempt to extract and upload the image to AWS S3.
        image_element = content_body.find("img")
        images = []
        if image_element:
            image_url = image_element.get("src")
            image_url, s3_key = upload_file_to_aws_s3(image_url)
            if image_url and s3_key:
                images = [image_url]
        # Update the dictionary with the extracted details.
        data.update({"name": title, "description": description, "images": images})

        return data

    def scrape_data_floridaattractions_site(self, html_content):
        """
        Extract relevant information from the Florida Attractions site's HTML content.

        This function processes the provided HTML content to retrieve details such as the attraction name,
        description, image, and other metadata from the Florida Attractions website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """

        # Extract attraction name.
        attraction_name = html_content.body['data-page-alias']

        # Extract attraction description.
        description = html_content.find('div', class_='dmNewParagraph').find('p').span.text.strip()

        # Attempt to extract and upload the image to AWS S3.
        img_tag = html_content.find('img', {'id': '1011350015'})
        images = []
        if img_tag:
            img_url = img_tag.get('src')
            image_url, s3_key = upload_file_to_aws_s3(img_url)
            if image_url and s3_key:
                images = [image_url]

        # Extract location data.
        div_element = html_content.find('div', class_='default')
        address = div_element.get('geocompleteaddress')
        meta_data = {"scraped_from": self.url}
        if address:
            meta_data["address"] = address

        # Construct and return the scraped data dictionary.
        scrape_data = {
            "name": attraction_name,
            "description": description,
            "latitude": div_element.get('lat'),
            "longitude": div_element.get('lon'),
            "meta_data": meta_data,
            "images": images
        }

        return scrape_data

    def scrape_data_visitflorida_site(self, html_content):
        """
        Extract relevant information from the Visit Florida site's HTML content.

        This function processes the provided HTML content to retrieve details such as the camp name,
        description, image, and other metadata from the Visit Florida site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}
        # Extract Camp name.
        title = html_content.find("h1")
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract attraction description.
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                             AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36")
        driver = webdriver.Chrome(options=options)
        driver.get(self.url)
        description_tab = driver.find_element(By.ID, "descriptionTab")
        if description_tab:
            content = description_tab.text.replace("\n", " ")
            scrape_data.update({"description": content.strip()})

        # Extract location data.
        city_state_zip_span = html_content.find('span', class_='city-state-zip')
        lat, long = get_geo_code(city_state_zip_span.get_text())
        scrape_data.update({"latitude": lat, "longitude": long})

        # Attempt to extract and upload the image to AWS S3.
        image_class = html_content.find(class_="gallery")
        image_element = image_class.find("img")
        if image_element:
            image_url, s3_key = upload_file_to_aws_s3(image_element.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": [image_url]})

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_atlasobscura_site(self, html_content):
        """
        Extract relevant information from the Atlasobscura site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Weird and Wicky Info,
        description, image, and other metadata from the Atlasobscura site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Weird and Wicky name.
        title = html_content.find("h1")
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract Weird and Wicky description.
        about = html_content.find(class_="DDP__body-copy")
        if about:
            scrape_data.update({"description": about.get_text().replace("\n", " ")})

        # Extract location data.
        address = html_content.find(class_="DDPage__header-place-location")
        if address:
            lat, long = get_geo_code(address.find("a").get_text())
            scrape_data.update({"latitude": lat, "longitude": long})

        # Attempt to extract and upload the image to AWS S3.
        image_body = html_content.find(class_="DDPage__item-gallery-container item-gallery-container hidden-print")
        image_element = image_body.find("img")
        if image_element:
            image_url, s3_key = upload_file_to_aws_s3(image_element.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": [image_url]})

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_biltmorehotel_site(self, html_content):
        """
        Extract relevant information from the Bilt More Hotel site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Weird and Wicky Info,
        description, image, and other metadata from the Atlasobscura site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Weird and Wicky name.
        title = html_content.find('div', class_='h1 home-slider-headline fg-white')
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract Weird and Wicky description.
        about_element = html_content.find(class_="paragraphs")
        about_element_two = html_content.find(class_="content-big-image")
        if about_element or about_element_two:
            scrape_data.update({"description": about_element.get_text().replace("\n", " ") +
                                               about_element_two.find("p").text.replace("\n", " ")})

        # Extract location data.
        location_class = html_content.find(class_="contac-info")
        if location_class:
            lat, long, address = get_geo_code_area(location_class.get_text())
            scrape_data.update({"latitude": lat, "longitude": long})
            meta_data.update({"address": address})

        # Attempt to extract and upload the image to AWS S3.
        image_body = html_content.find('picture')
        image_element = image_body.find("img")
        if image_element:
            image_url, s3_key = upload_file_to_aws_s3(image_element.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": [image_url]})

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_myfishermancove_site(self, html_content):
        """
        Extract relevant information from the My Fisher Manscove site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Weird and Wicky Info,
        description, image, and other metadata from the Atlasobscura site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Weird and Wicky name.
        title = html_content.find('title')
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract location data.
        location_class = html_content.find(class_="contac-info")
        if location_class:
            lat, long, address = get_geo_code_area("Orlando")
            scrape_data.update({"latitude": lat, "longitude": long})
            meta_data.update({"address": address})

        # Attempt to extract and upload the image to AWS S3.
        image_element = html_content.find(class_="elementor-element\
                                          elementor-element-4e638b79\
                                          elementor-widget elementor-widget-image")
        if image_element:
            img_data = image_element.find('img')
            image_url, s3_key = upload_file_to_aws_s3(img_data.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": image_url})

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_visitpanamacitybeach_site(self, html_content):
        """
        Extract relevant information from the Panama City Beach site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Weird and Wicky Info,
        description, image, and other metadata from the Atlasobscura site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Title.
        title = html_content.find("h1")
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract description.
        main_content = html_content.find(class_="content")
        if main_content:
            content = "".join(main_content.stripped_strings)
            scrape_data.update({"description": content})

        # Extract location data.
        lat, long = get_geo_code("Panama City Beach")
        scrape_data.update({"latitude": lat, "longitude": long})

        # Attempt to extract and upload the image to AWS S3.
        image_element = html_content.find(class_="img-cont")
        if image_element:
            img_data = image_element.find('img')
            image_url, s3_key = upload_file_to_aws_s3(img_data.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": image_url})
        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_floridadiving_site(self, html_content):
        """
        Extract relevant information from the Florida Diving Beach site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Weird and Wicky Info,
        description, image, and other metadata from the Florida Diving Beach site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Title.
        title = html_content.find("h1")
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract description.
        main_content = html_content.find(class_="entry-content")
        if main_content:
            scrape_data.update({"description": main_content.get_text().replace("\n", " ")})

        # Extract location data.
        lat, long = get_geo_code("Tampa")
        scrape_data.update({"latitude": lat, "longitude": long})

        # Attempt to extract and upload the image to AWS S3.
        image_element = html_content.find(class_='events-header').find_all('picture')
        if image_element:
            img_data = image_element.find('img')
            image_url, s3_key = upload_file_to_aws_s3(img_data.get("src"))
            if image_url and s3_key:
                scrape_data.update({"images": image_url})

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_visittampabay_site(self, html_content):
        """
        Extract relevant information from the Visit Tampa Bay site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Visit Tampa Bay site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}

        # Extract Title.
        title = html_content.find("h1")
        if title:
            scrape_data.update({"name": title.get_text()})

        # Extract description.
        description = html_content.find(class_="columns")
        if description:
            scrape_data.update({"description": description.find("p").get_text()})

        # Extract location data.
        lat, long = get_geo_code("Tampa")
        scrape_data.update({"latitude": lat, "longitude": long})

        # Attempt to extract and upload the image to AWS S3.
        # No Image
        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_ledgernews_site(self, html_content):
        """
        Extract relevant information from the Ledger News site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Visit Ledger News site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scraped_from": self.url}
        published_time = html_content.find('div', class_='gnt_ar_dt')['aria-label']
        if published_time:
            meta_data.update({"published_time": published_time})

        # Extract Title.
        title_tag = html_content.find('title')
        if title_tag:
            scrape_data.update({"name": title_tag.get_text()})

        # Extract description.
        description = html_content.find(class_='gnt_ar_b')
        if description:
            scrape_data.update({"description": description.get_text()})

        # Extract location data.
        lat, long = get_geo_code("Miami")
        scrape_data.update({"latitude": lat, "longitude": long})

        # No Image

        scrape_data.update({"meta_data": meta_data})
        return scrape_data

    def scrape_data_eventbrite_site(self, html_content):
        """
        Extract relevant information from the Event Brite site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Event Brite site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        description_element = html_content.find(class_="eds-text-bm eds-l-mar-vert-4 spaced-paragraphs")
        if description_element:
            description = description_element.text
        cover_image_element = html_content.find(class_="city-browse-header__image--container")
        if cover_image_element:
            image_url = cover_image_element.find("img")
            image_url = image_url.get("src")
        scrape_data = []
        for element in html_content.find_all("div", class_="small-card-mobile eds-l-pad-all-2"):
            each_event = {"latitude": None, "longitude": None}
            event_title_element = element.find(class_="Stack_root__1ksk7")
            for item in event_title_element:
                if item.find("h2"):
                    each_event.update({"title": item.find("h2").get_text()})
            extra_info = event_title_element.get_text()
            meta_data = {"scraped_from": self.url, "extra_info": extra_info}
            image_element = element.find(class_="event-card-image__aspect-container").find("img")
            image_url = image_element.get("src")+".png"
            image_url, s3_key = upload_file_to_aws_s3(image_url, raw_url=True)
            if image_url and s3_key:
                each_event.update({"images": [image_url]})
            each_event.update({"meta_data": meta_data,
                               "description": description})
            scrape_data.append(each_event)
        return scrape_data

    def scrape_data_wakesurftampabay_site(self, html_content):
        """
        Extract relevant information from the Wake Surf TampaBay site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Wake Surf TampaBay site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}
        meta_data = {"scrapped_from": self.url}
        # Find the paragraph tag containing the desired text
        text_span = html_content.find('span', class_='s2')

        description = text_span.text

        # Find the img tag
        img_tag = html_content.find_all('img', class_='swiper-slide-image')

        images = []
        for img in img_tag:
            image_url, s3_key = upload_file_to_aws_s3(img['src'])
            if image_url and s3_key:
                images.append(image_url)

        # Find the title tag
        title_tag = html_content.find('title')
        name = title_tag.text

        # Find the geo address
        geo_dt, api_data = helper.get_geo_data(name)

        meta_data.update({"address": api_data})

        # Construct and return the scraped data dictionary.
        scrape_data = {
            "name": name,
            "description": description,
            "latitude": geo_dt.get("latitude"),
            "longitude": geo_dt.get("longitude"),
            "meta_data": meta_data,
            "images": images
        }

        return scrape_data

    def scrape_data_theliftadventurepark_site(self, html_content):
        """
        Extract relevant information from the Wake Surf TampaBay site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Wake Surf TampaBay site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}

        images = []
        meta_data = {"scrapped_from": self.url}
        image_element = html_content.find(class_="img-wrap")
        if image_element:
            image_url, s3_key = upload_file_to_aws_s3(image_element.find("img").get("src"))
            if image_url and s3_key:
                images.append(image_url)

        # If found, parse the JSON data
        ld_json_data = []
        script_tag = html_content.find_all('script', type="application/ld+json")
        for i in script_tag:
            if i:
                json_data = json.loads(i.string)
                ld_json_data.append(json_data)

        webpage_data = ld_json_data[0]['@graph'][0]

        name = webpage_data['name']
        description = webpage_data['description']

        # Find the geo address
        geo_dt, api_data = helper.get_geo_data(name)

        meta_data.update({"address": api_data})

        # Construct and return the scraped data dictionary.
        scrape_data = {
            "name": name,
            "description": description,
            "latitude": geo_dt.get("latitude"),
            "longitude": geo_dt.get("longitude"),
            "meta_data": meta_data,
            "images": images
        }
        return scrape_data

    def scrape_data_visitlauderdale_site(self, html_content):
        """
        Extract relevant information from the Visit Lauderdale site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Visit Lauderdale site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """
        scrape_data = {}

        images = []
        meta_data = {"scrapped_from": self.url}

        # Extract title and description
        h1_element = html_content.find('h1')
        p_elements = html_content.find_all('p')

        # Extract text content from elements
        name = h1_element.text if h1_element else None
        description_element = [p.text for p in p_elements if len(p) != 0]
        description = description_element[2:]

        # Extract image content 
        image_element = str(html_content.find(class_="footer-container"))
        match = re.search(r'background-image: url\("([^"]+)"\);', image_element)

        if match:
            background_image_url = match.group(1)
            image_url, s3_key = upload_file_to_aws_s3(background_image_url)
            if image_url and s3_key:
                images.append(image_url)

        # Find the geo address
        geo_dt, api_data = helper.get_geo_data(name)
        meta_data.update({"address": api_data})

        # Construct and return the scraped data dictionary.
        scrape_data = {
            "name": name,
            "description": description,
            "latitude": geo_dt.get("latitude"),
            "longitude": geo_dt.get("longitude"),
            "meta_data": meta_data,
            "images": images
        }
        return scrape_data

    def scrape_data_stranahanhouse_site(self, html_content):
        """
        Extract relevant information from the Strana House site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the Strana House site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """

        scrape_data = {}

        meta_data = {"scrapped_from": self.url}

        script_tag = html_content.find_all('script', type="application/ld+json")

        description_element = html_content.find(class_="col-inner")

        # Extract text content from elements
        description = ' '.join(description_element.get_text().split())

        # If found, parse the JSON data
        ld_json_data = []

        for item in script_tag:
            if item:
                json_data = json.loads(item.string)
                ld_json_data.append(json_data)

        name = ld_json_data[0]['name']
        image = ld_json_data[1]['image']

        # Extract Images
        images = []
        if image:
            image_url, s3_key = upload_file_to_aws_s3(image)
            if image_url and s3_key:
                images.append(image_url)

        # Find the geo address
        geo_dt, api_data = helper.get_geo_data(name)
        meta_data.update({"address": api_data})

        # Construct and return the scraped data dictionary.
        scrape_data = {
            "name": name,
            "description": description,
            "latitude": geo_dt.get("latitude"),
            "longitude": geo_dt.get("longitude"),
            "meta_data": meta_data,
            "images": images
        }

        return scrape_data


    def scrape_data_mbtallahassee_site(self, html_content):
        """
        Extract relevant information from the mbtallahassee site's HTML content.

        This function processes the provided HTML content to retrieve details such as the Events Info,
        description, image, and other metadata from the mbtallahassee site website. The extracted details
        are then organized and returned in a dictionary format.

        Args:
        - html_content (BeautifulSoup object): The BeautifulSoup parsed HTML content of the target webpage.

        Returns:
        - dict: A dictionary containing the extracted details including name, description, image, and other metadata.
        """

        scrape_data = {}
        meta_data = {"scrapped_from": self.url}
        li_elements = html_content.find_all(class_="site-content")

        # Iterate through each li element and extract heading and image
        images = []

        for li in li_elements:
            heading = li.find('h3').text
            para = li.find('p').text

            image_url = li.find('img')['src']
            if image_url:
                image_url, s3_key = upload_file_to_aws_s3(image_url)
                if image_url and s3_key:
                    images.append(image_url)

            scrape_data.update({"name":heading, "description":para, 
                                "images":images, "meta_data": meta_data,
                                "latitude":None, "longitude":None})
        return scrape_data

    def scrape_data(self):
        """
        Scrapes data from various websites based on the provided URL.

        This function first fetches the content of the given URL and then based on the domain
        of the URL, chooses an appropriate scraping function to extract data from the website.

        Returns:
        - dict: A dictionary containing scraped data from the given URL.

        Raises:
        - Exception: If there's any issue during the HTTP request or scraping process.
        """
        # Common headers to mimic a real browser request.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.82 Safari/537.36'
        }

        try:
            # Send a GET request to the provided URL with the headers.
            response = requests.get(self.url, headers=headers)
            # Raise an HTTPError if the HTTP request returned an unsuccessful status code.
            response.raise_for_status()

            # Parse the HTML content of the response.
            html_content = BeautifulSoup(response.text, 'html.parser')

            # Extract the domain from the URL for deciding which scraper function to use.
            domain = self.url.split('/')[2]
            scrape_data = {}

            # Map each domain to its respective scraping function.
            scraper_function_map = {
                Constant.MIAMI_BEACH_SITE: self.scrape_data_from_miami_beach_site,
                Constant.RESTAURANT_SITE: self.scrape_data_from_restaurantji_site,
                Constant.VISITORLANDO_SITE: self.scrape_data_from_visitorlando_site,
                Constant.FLORIDA_STATE_SITE: self.scrape_data_floridastateparks_site,
                Constant.FLORIDA_ATTRACTIONS_SITE: self.scrape_data_floridaattractions_site,
                Constant.VISITFLORIDA_SITE: self.scrape_data_visitflorida_site,
                Constant.ATLASOBSCURA_SITE: self.scrape_data_atlasobscura_site,
                Constant.BITLMOREHOTEL_SITE: self.scrape_data_biltmorehotel_site,
                Constant.MYFISHERMANSCOVE_SITE: self.scrape_data_myfishermancove_site,
                Constant.VISITPANAMACITYBEACH_SITE: self.scrape_data_visitpanamacitybeach_site,
                Constant.FLORIDADIVING_SITE: self.scrape_data_floridadiving_site,
                Constant.VISITTAMPABAY_SITE: self.scrape_data_visittampabay_site,
                Constant.LEDGERNEWS_SITE: self.scrape_data_ledgernews_site,
                Constant.EVENT_BRITE: self.scrape_data_eventbrite_site,
                Constant.WAKESURFTAMPABAY: self.scrape_data_wakesurftampabay_site,
                Constant.THELIFTADVENTUREPARK_SITE: self.scrape_data_theliftadventurepark_site,
                Constant.VISITLAUDERDALE: self.scrape_data_visitlauderdale_site,
                Constant.STRANAHANHOUSE_SITE: self.scrape_data_stranahanhouse_site,
                Constant.MBTALLAHASSEE: self.scrape_data_mbtallahassee_site

            }

            # Calling the appropriate scraping function based on the domain.
            if domain in scraper_function_map:
                scrape_data = scraper_function_map[domain](html_content)

            return scrape_data

        except Exception as ex:
            raise Exception(f"Failed to scrape data due to: {ex}")
