#!/usr/bin/env python3

import sys
import os
from PIL import Image

# Format the images to the specifications required by the supplier and/or website requirements.

def process_image():

    # Path to images.
    image_path = "/home/student-00-17a94b58acdf/supplier-data/images/"

    # For each image that needs to be formatted, modify to specifications below.
    for image in os.listdir(image_path):
        try:
            img = Image.open(image_path + image)
            img.resize((600, 400)).convert("RGB").save(image_path + "/" + image.split('.')[0] + "." + "jpeg")
            img.close()
                
        # If a non-image file is located, skip and hide error message.
        except IOError:
            continue

def main(argv):
    
    formatting = process_image()

if __name__ == "__main__":
    main(sys.argv)