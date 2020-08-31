#!/usr/bin/env python3

# Called by report_email.py.

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Create the PDF template to be utilized in report_email.py

def generate_report(filename, title, para):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles['h1'])
    content  = Paragraph(para, styles['BodyText'])
    new_line = Spacer(1,20)
    report.build([report_title, new_line, content])