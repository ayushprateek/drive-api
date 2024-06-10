import concurrent.futures

import boto3
from botocore.config import Config

import re
from apps.user import models as user_model
from drive_ai import settings
import requests
import os
from urllib.parse import urlparse

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
    config=Config(s3={"addressing_style": "path"}, signature_version="s3v4"),
)


def generate_file_key(file_type, file, content_type):
    """just renaming the file before uploading"""
    """Please Set Folder Name In Constants"""

    # _, ext = os.path.splitext(file)
    url = "{}/{}/{}".format(settings.AWS_MEDIA_PATH, file_type, file, content_type)
    return url


class S3GenerateSignedUrl:
    """Generate s3 signed URL"""

    def __init__(self, key):
        self.key = key

    def generate_signed_url(self):
        url = s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": settings.AWS_BUCKET, "Key": "{}".format(self.key)},
            ExpiresIn=604800,
        )
        return url


def convert_s3_key_to_s3_signed_url(s3_key=None):
    """Function to Convert S3_Key to Signed URL"""
    s3_url = None
    if s3_key and s3_key.startswith(settings.AWS_MEDIA_PATH):
        s3_url = S3GenerateSignedUrl(s3_key).generate_signed_url()
        s3_url = s3_url.split("?")[0]
    return s3_url


def convert_image_id_to_s3_signed_url(image_id):
    """Fetch Signed URL using Image ID"""
    if image_id:
        obj = user_model.Media.get_instance_or_none({"id": image_id})
        return convert_s3_key_to_s3_signed_url(obj.media_key) if obj else None
    return None


class S3Object:
    def __init__(self, file, file_type, content_type):
        self.file = file
        self.file_type = file_type
        self.content_type = content_type

    def upload(self):
        key = generate_file_key(self.file_type, self.file, self.content_type)

        s_3 = boto3.resource(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        s_3.Object(settings.AWS_BUCKET, key).put(Body=self.file)

        return key


def upload_file_to_aws_s3(url='', file_type='image', raw_url=None):
    """
    Read the scraped image URL and upload it s3 bucket
    and will return the file url
    """
    file_url, key = key = None, None

    # get the connection of AWS S3 Bucket
    s_3 = boto3.resource(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_REGION
    )
    try:
        response = requests.get(url)
        if response.status_code == 200:
            raw_data = response.content
            url_parser = urlparse(url)
            file_name = os.path.basename(url_parser.path)
            cleaned_filename = re.sub(r'[^a-zA-Z0-9.]', '', file_name)
            if raw_url:
                key = file_type + "/" + cleaned_filename+".jpg"
            else:
                key = file_type + "/" + cleaned_filename
        else:
            return None, None
        # Write the raw data as byte in new file_name in the server
        with open(file_name, 'wb') as new_file:
            new_file.write(raw_data)

        # Open the server file as read mode and upload in AWS S3 Bucket.
        data = open(file_name, 'rb')
        s_3.Bucket(settings.AWS_BUCKET).put_object(Key=key, Body=data, ACL='public-read')
        data.close()

        # Format the return URL of upload file in S3 Bucket
        file_url = f"https://s3.amazonaws.com/{settings.AWS_BUCKET}/" + key

        # Close and remove file from Server
        new_file.close()
        os.remove(file_name)

    except Exception as e:
        pass

    return file_url, key


def upload_website_scrapped_data(key, file):
    """Upload"""

    s_3 = boto3.resource(
        "s3",
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )

    s_3.Object(settings.AWS_BUCKET, key).put(Body=file, ACL='public-read')

    return key


def get_file_content(s3_key):
    s_3 = boto3.resource(
        "s3",
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    obj = s_3.Object(settings.AWS_BUCKET, s3_key)

    content = obj.get()['Body'].read().decode('utf-8')
    return content


def upload_hotel_images_to_s3(image, folder='hotel-images'):
    try:
        s_3 = boto3.resource(
            "s3",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )
        response = requests.get(image)
        if response.status_code == 200:
            raw_data = response.content
            url_parser = urlparse(image)
            file_name = os.path.basename(url_parser.path)
            key = folder + "/" + file_name
        else:
            return None
        # Write the raw data as byte in new file_name in the server
        with open(file_name, 'wb') as new_file:
            new_file.write(raw_data)

        # Open the server file as read mode and upload in AWS S3 Bucket.
        data = open(file_name, 'rb')
        s_3.Bucket(settings.AWS_BUCKET).put_object(Key=key, Body=data, ACL='public-read')
        data.close()

        # Close and remove file from Server
        new_file.close()
        os.remove(file_name)
        return key
    except Exception:
        pass


def process_hotel_images(images):
    image_keys = []
    folder = 'hotel-images'
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # submit the tasks
        futures = {executor.submit(upload_hotel_images_to_s3, image, folder): image for image in images}

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()  # this will block until the specific future is complete
                if result:
                    image_keys.append(result)
            except Exception as exc:
                pass

    return image_keys
