from analytics_service_object import initialize_service
from convert_pdf import convertHtmlToPdf
from get_social import get_minutes_seconds
from private_data import profile_id
import datetime

today = datetime.datetime.now()
today = today.replace(day=1)
lastMonth = today - datetime.timedelta(days=1)
lastMonth = lastMonth.replace(day=1)

def get_mail_campaigns_report(service, profile_id, start_date, end_date):
    total = 0
    cleaned = []
    ids = 'ga:' + profile_id
    metrics = 'ga:sessions, ga:bounceRate, ga:avgSessionDuration'
    dimensions = 'ga:campaign, ga:landingPagePath'
    data = service.data().ga().get(
        sort='ga:campaign, ga:sessions' ,ids=ids, start_date=start_date, end_date=end_date, 
        metrics=metrics, dimensions=dimensions).execute()
    for campaign, landing, value, bounce, duration in data['rows']:
        if campaign != '(not set)':
            cleaned.append([campaign, landing, value, bounce, get_minutes_seconds(duration)])
            total = total + int(value)
    return {'data': cleaned, 'start_date' : start_date, 'end_date' : end_date, 'total' : total}

if __name__ == '__main__':
    service = initialize_service()
    start_date = lastMonth.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    data = get_mail_campaigns_report(service, profile_id, start_date, end_date)
    print data
    convertHtmlToPdf(data, 'ga/templates/mail.html', "mail.pdf")
