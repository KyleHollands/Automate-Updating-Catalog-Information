#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails
import glob

date = date.today() # Acquire the current date.
title = "Processed Update on {}".format(date) # Define the title of the PDF with the date acquired prior.

# Acquire all of the text files in the descriptions directory.
text_files = glob.glob("/home/student-00-17a94b58acdf/supplier-data/descriptions/*.txt")
txt_list = []

# Loop through all text files in the descriptions directory.
for files in text_files:
    with open(files,"r") as f:
        reader = f.read().split("\n") # Split the lines at the newline markers.
        txt_list.append(reader) # Creating a list of lists from the text data.

# Acquiring the body of the PDF from the txt_list.
para_g = ""
mesg = ""

for fields in txt_list:
    mesg = "name: {}<br/> weight: {}<br/><br/>".format(fields[0],fields[1]) # Acquire the name and weight values only.
    para_g = para_g + mesg

if __name__ == "__main__":
    
    # Acquiring all required values for sending the email.

    sender = "automation@example.com"
    recipient = "student-00-17a94b58acdf@example.com"
    subject = " Upload Completed - Online Fruit Store "
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"

    reports.generate_report("/tmp/processed.pdf",title,para_g)  # Call generate_report from reports.py and create the PDF.
    msg = emails.generate_email(sender, recipient, subject, body, attachment_path) # Call generate_email from emails.py to create the email template.
    emails.send_email(msg) # Call send_email in emails.py to send the email.