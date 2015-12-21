#!/usr/bin/env python
# -*- coding: utf-8 -*-
from analytics_service_object import initialize_service
from get_mail import get_mail_campaigns_report
from get_social import get_social_report
from convert_pdf import convertHtmlToPdf
from private_data import profile_id
import datetime

today = datetime.datetime.now()
today = today.replace(day=1)
lastMonth = today - datetime.timedelta(days=1)
lastMonth = lastMonth.replace(day=1)

if __name__ == '__main__':
    service = initialize_service()
    start_date = lastMonth.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    mail_data = get_mail_campaigns_report(service, profile_id, start_date, end_date)
    social_data = get_social_report(service, profile_id, start_date, end_date)
    convertHtmlToPdf(mail_data, 'ga/templates/mail.html', "mail.pdf")
    convertHtmlToPdf(social_data, 'ga/templates/social.html', "social.pdf")