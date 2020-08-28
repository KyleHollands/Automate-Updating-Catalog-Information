#!/usr/bin/env python3

import sys
import os
from PIL import Image

# Format the images to the specifications required by the supplier and/or website requirements.

def process_image():
    # For each image that needs to be formatted, modify to specifications below.
    image_path = (os.getcwd() + "\supplier-data\images\\")
    for image in os.listdir(image_path):
        try:
            img = Image.open(image_path + image)
            img.resize((600, 400)).convert("RGB").save(image_path + "/" + image.split('.')[0] + "." + ".JPEG")
            img.close()
                
        # If a non-image file is located, skip and hide error message.
        except OSError:
            continue

def main(argv):
    # Location of supplier images that need to be formatted.

    formatting = process_image()

if __name__ == "__main__":
    main(sys.argv)