import requests
from bs4 import BeautifulSoup
from apps.user.models import Media
from common import cloud_service


def scrap_images(instance=None, url=None):
    """
    This function is designed to extract images from a source URL,
    returning the media object while also saving the extracted
    content in an S3 blob."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    infobox = soup.find("table", class_="infobox")
    media_url, description = None, None
    if infobox:
        image = infobox.find("img")
        if image:
            src_url = image.get("src")
            media_url, media_key = cloud_service.upload_file_to_aws_s3("https:" + src_url)

    # Find all <p> tags
    paragraphs = soup.find_all('p')
    if len(paragraphs) >= 4:
        description = " ".join([paragraph.text.strip() for paragraph in paragraphs[:4]])
    return media_url, description
