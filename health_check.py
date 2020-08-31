#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails
import sys

# Send an email if an error occurs.
def error_mail(subject_line):
    sender = "automation@example.com"
    recipient = "student-00-17a94b58acdf@example.com"
    subject = subject_line
    body = "Please check your system and resolve the issue as soon as possible."

    msg = emails.generate_error_report(sender, recipient, subject, body) # Call generate_error_report in emails.py with the prior attributes.
    emails.send_email(msg) # Send error report to recipient with the send_email function in emails.py.

#----------------------------------------------------------------------------------------------

# Check if disk usage is less than 20%. If so, call error_mail function.
def check_disk_usage():
    du = shutil.disk_usage("/")
    free_percent = du.free/du.total*100
    if free_percent < 20:
        subject_line = "Error - Available disk space is less than 20%"
        error_mail(subject_line)

# Check if cpu usage exceeds 80%. If so, call error_mail function.
def check_cpu_percent():
    usage = psutil.cpu_percent(1)
    if usage > 80:
        subject_line = "Error - CPU usage is over 80%"
        error_mail(subject_line)

# Check if available memory is less than the 500mb threshold. If so, call error_mail function.
def check_RAM_mem():
    RAM_data = psutil.virtual_memory().available
    avail_mem = RAM_data // (1024 ** 2)
    if avail_mem < 500:
        subject_line = "Error - Available memory is less than 500MB"
        error_mail(subject_line)

# Check if the localhost ip address can be resolved. If not, call error_mail function.
def check_ip():
    ip_addr = socket.gethostbyname("localhost")
    if ip_addr != "127.0.0.1":
        subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
        error_mail(subject_line)


def main(argv):
    check_disk_usage()
    check_cpu_percent()
    check_RAM_mem()
    check_ip()
    
if __name__ == "__main__":
    main(sys.argv)