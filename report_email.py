#!/usr/bin/env python3

import os
from datetime import date
import sys
import emails

from reportlab.platypus import paragraph
import reports
import glob


def process_data(curr_date, report_title, txt_files, txt_list):
    for files in txt_files:
        with open(files, 'r') as f:
            reader = f.read().split("\n")
            txt_list.append(reader)

    paragraph = ""

    for data in txt_list:
        msg = ""
        msg = "Name: {}<br/> Weight:{}<br/><br/>".format(data[0], data[1])
        paragraph = paragraph + msg

def main(argv):
    curr_date = date.today() # Acquire current date and time.
    report_title = "Processed Update on {}".format(date) # Title of report.
    # txt_files = glob.glob("path/*.txt")
    txt_files = glob.glob(r"C:\Users\kyleh\OneDrive\Education\Coursera\Google IT Automation with Python\Automating Real-World Tasks with Python\Week 4\Resources\Automating Updating Catalog Information\supplier-data\descriptions\\*.txt")
    txt_list = []

    processing = process_data(curr_date, report_title, txt_files, txt_list)

    sender = "automation@example.com"
    recipient = "student url"
    subject = " Online Fruit Store Upload Completed "
    body = "Fruits have been uploaded to the website successfully. An attached email with a detailed list is included."
    attachment_path = "attachment directory"

    reports.generate_report("pdf path", report_title, paragraph)
    message = emails.generate_email(sender, recipient, subject, body, attachment_path)
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)