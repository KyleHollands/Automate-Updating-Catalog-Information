#!/bin/usr/env python3

import PIL
import requests
import reportlab
import email
import shutil
import smtplib
import sys
import os

# Images formatted and uploaded separately to a different web endpoint.
def image_processing(img_file):
    pass



# Descriptions formatted and uploaded separately to a different web endpoint.
def description_processing(desc_file):
    pass



def report_creation():
    pass



def send_report():
    pass



def main(argv):
    # Process images.
    # Call image_processing() function.
    images = image_processing("/images/")

    # Process descriptions.
    # Call description_processing() function.
    descriptions = description_processing("/descriptions/")

    # Create PDF report.
    # Call report_creation() function.
    create_report = report_creation()

    # Send PDF report.
    # Call send_report() function.
    email_report = send_report()





    pass

if __name__ == "__main__":
    main(sys.argv)