#!/usr/bin/env python3

import sys
import requests
import os
from PIL import Image

# Upload the previously formatted images to the web endpoint.

def upload_image():
    url = "http://35.239.145.178/upload/"

    # Windows path.
    # image_path = (os.getcwd() + "\supplier-data\images\\")

    # Linux project path.
    image_path = "/home/student-00-17a94b58acdf/supplier-data/images/"

    # Open and upload each image in the specified directory.
    for image in os.listdir(image_path):
        if image.lower().endswith('.jpeg'):
            try:
                with open(image_path + "/" + image, 'rb') as opened:
                    requests.post(url, files={'file': opened})
            except IOError:
                continue

def main(argv):
    
    upload = upload_image()
    
if __name__ == "__main__":
    main(sys.argv)