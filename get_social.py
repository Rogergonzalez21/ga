from analytics_service_object import initialize_service
from convert_pdf import convertHtmlToPdf
from private_data import profile_id
import datetime

today = datetime.datetime.now()
today = today.replace(day=1)
lastMonth = today - datetime.timedelta(days=1)
lastMonth = lastMonth.replace(day=1)

def get_minutes_seconds(seconds):
    time = datetime.timedelta(seconds=float(seconds))
    minutes = (time.seconds % 3600) // 60
    seconds = (time.seconds % 60)
    if len(str(seconds)) == 1:
        seconds = '0%s' % seconds
    time = "%s:%s" % (minutes, seconds)
    return time

def get_social_report(service, profile_id, start_date, end_date):
    total = 0
    total_fb = 0
    total_tw = 0
    total_lkin = 0
    total_others = 0
    cleaned = []
    ids = 'ga:' + profile_id
    metrics = 'ga:sessions, ga:bounceRate, ga:avgSessionDuration'
    dimensions = 'ga:socialNetwork, ga:landingPagePath'
    data = service.data().ga().get(
        sort='ga:socialNetwork, ga:sessions' ,ids=ids, start_date=start_date, end_date=end_date, 
        metrics=metrics, dimensions=dimensions).execute()
    for source, landing, value, bounce, duration in data['rows']:
        if source != '(not set)':
            cleaned.append([source, landing, value, bounce, get_minutes_seconds(duration)])
            if source == 'Facebook':
                total_fb = total_fb + int(value)
            elif source == 'Twitter':
                total_tw = total_tw + int(value)
            elif source == 'LinkedIn':
                total_lkin = total_lkin + int(value)
            else:
                total_others = total_others + int(value)

            total = total + int(value)

    return {'data': cleaned, 'start_date' : start_date, 'end_date' : end_date, 'total' : total, 
    'total_fb' : total_fb, 'total_tw' : total_tw, 'total_lkin' : total_lkin, 'total_others' : total_others}

if __name__ == '__main__':
    service = initialize_service()
    start_date = lastMonth.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    data = get_social_report(service, profile_id, start_date, end_date)
    print data
    convertHtmlToPdf(data, 'ga/templates/social.html', "social.pdf")
