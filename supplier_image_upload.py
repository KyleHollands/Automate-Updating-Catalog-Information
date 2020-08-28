#!/usr/bin/env python3

import sys
import requests
import os
from PIL import Image

# Upload the previously formatted images to the web endpoint.

def upload_image():
    url = "http://34.122.246.131/upload/"

    # Windows path.
    # image_path = (os.getcwd() + "\supplier-data\images\\")

    # Linux project path.
    image_path = "/home/student-00-e379d8f14a7e/supplier-data/images/"

    # Open and upload each image in the specified directory.
    for image in os.listdir(image_path):
        try:
            with open(image_path + "/" + image, 'rb') as opened:
                requests.post(url, files={'file': opened})
        except IOError:
            continue

def main(argv):
    # Location of supplier images that need to be formatted.
    
    upload = upload_image()
    
if __name__ == "__main__":
    main(sys.argv)