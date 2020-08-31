#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(file, title, add_info):
    styles = getSampleStyleSheet
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    new_line = Spacer(1, 20)
    report.build([report_title, new_line, report_info])