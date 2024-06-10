import requests
import re
from bs4 import BeautifulSoup
from apps.trip import models as trip_models
from apps.trip.services.common import get_geo_code_area

from apps.user.models import Media
from common.cloud_service import upload_file_to_aws_s3


# Input URL

def find_domain(url):
    # Use regular expression to extract "CDNDOMAIN6"
    match = re.search(r'CDNDOMAIN(\d+)', url)
    if match:
        cdn_domain = match.group(0)
        match = re.match(r"([a-zA-Z]+)(\d+)", cdn_domain)
        output_url = re.sub(r'CDNDOMAIN\d+', f"cdn{match.group(2)}.localdatacdn.com", url)
        return output_url
    else:
        return ""

def get_hotel_metadata(instance=None, url=None):
    """
    Getting metadata of all the hotels available in the city"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all restaurant listings on the page
    restaurant_listings = soup.find_all(class_="strip grid")
    count = 0
    for item in restaurant_listings:
        count +=1
        obj_data = {}
        try:
            location = item.find(class_="wrapper").find("small")
            latitude, longitude, address = get_geo_code_area(location.get_text())
            obj_data.update({"name":item.find(class_="read_more").get_text(),
                        "latitude":latitude, "longitude":longitude, 
                        "description":item.find('p').get_text(),
                        "city":instance})
            image_element = item.find("img")
            if image_element:
                image_url = image_element.get("data-src")
                modified_image_url = find_domain(image_url)
                media_url, media_key = upload_file_to_aws_s3(modified_image_url)
                media_obj = Media.create_instance({"media_url":media_url,
                                        "media_key":media_key})         
                obj_data.update({"image":media_obj})
            if count == 25: # Temp. cap, Will be removed
                break
            trip_models.Food.create_instance(obj_data)
        except Exception:
            pass