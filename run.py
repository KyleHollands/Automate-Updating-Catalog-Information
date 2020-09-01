#!/usr/bin/env python3

import os
import requests
import sys
import re

def post_products(url, descriptions_path, file_pattern, weight_pattern, number_pattern, product_keys):
    
    # Loop through the files in the descriptions directory.
    for description in os.listdir(descriptions_path):
        if re.search(file_pattern, description): # If the file ends with .txt.
            key_count = 0
            fruit = {}

            # Open the .txt file.
            with open(descriptions_path + description, 'r') as f:
                for line in f:
                    
                    value = line.strip()
                    if re.search(number_pattern, value): # If the file line starts with a number..
                        if re.search(weight_pattern, value):
                            value = re.sub(weight_pattern, '', value) # Strip off lbs from the weight line.
                            fruit[product_keys[key_count]] = int(value) # Add the integer weight value to the fruit dictionary utilizing explicit integer conversion.
                            key_count += 1
                    else:                                # If the file line doesn't start with a number, add it to the fruit dictionary.
                        fruit[product_keys[key_count]] = value
                        key_count += 1

                # Set the image_name key to the corresponding image file.
                fruit["image_name"] = description.split(".")[0] + ".jpeg"

                # Post the fruit dictionary / json file to the specified url.
                response = requests.post(url, json = fruit)

                # print(fruit)

def main(argv):
    
    # Path to descriptions.
    descriptions_path = "/home/student-00-17a94b58acdf/supplier-data/descriptions/"

    # Define keys to be used in the fruit dictionary.
    product_keys = ["name", "weight", "description", "image_name"]

    # Set patterns for the .txt files, stripping lbs off the weight value and whether the value starts with an integer.
    file_pattern = r'([0-9]{3}[.][a-z][.txt]+)'
    weight_pattern = r'([\D]+)'
    number_pattern = r'(^[\d]+)'

    # Url where the descriptions will be uploaded to.
    url = "http://35.239.145.178/fruits/"

    product_upload = post_products(url, descriptions_path, file_pattern, weight_pattern, number_pattern, product_keys)
    
if __name__ == "__main__":
    main(sys.argv)