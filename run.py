#!/usr/bin/env python3

import os
import requests
import sys
import re

def post_products(url, descriptions_path, file_pattern, weight_pattern, number_pattern, product_keys):
    
    for description in os.listdir(descriptions_path):
        if re.search(file_pattern, description):
            key_count = 0
            fruit = {}

            with open(descriptions_path + description, 'r') as f:
                for line in f:
                    
                    value = line.strip()
                    if re.search(number_pattern, value):
                        if re.search(weight_pattern, value):
                            value = re.sub(weight_pattern, '', value)
                            fruit[product_keys[key_count]] = int(value)
                            key_count += 1
                    else:
                        fruit[product_keys[key_count]] = value
                        key_count += 1

                    # if key_count != 1:
                    #     fruit[product_keys[key_count]] = line.strip()
                    #     key_count = key_count + 1
                    # else:
                    #     fruit[product_keys[key_count]] = line.strip()[:-4]
                    #     key_count = key_count + 1

                fruit["image_name"] = description.split(".")[0] + ".jpeg"

                response = requests.post(url, json = fruit)

                print(fruit)

def main(argv):

    # Windows path.
    descriptions_path = (os.getcwd() + "\supplier-data\descriptions\\")
    
    # Linux project path
    descriptions_path = "/home/student-00-e963a890acb9/supplier-data/descriptions/"

    product_keys = ["name", "weight", "description", "image_name"]

    # Set file pattern to look for .txt files.
    file_pattern = r'([0-9]{3}[.][a-z][.txt]+)'
    weight_pattern = r'([\D]+)'
    number_pattern = r'(^[\d]+)'
    url = "http://34.68.178.235/fruits/"

    product_upload = post_products(url, descriptions_path, file_pattern, weight_pattern, number_pattern, product_keys)
    
if __name__ == "__main__":
    main(sys.argv)