import datetime

def reformat_subway_dates(date):
    date_formatted = datetime.datetime.strptime(date, "%m-%d-%y").strftime("%Y-%m-%d")
    return date_formatted
