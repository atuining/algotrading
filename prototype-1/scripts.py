import datetime

# get next weekday closest to date
def get_weekday(date: datetime.date):
    if date.isoweekday() in set((6,7)):
        date += datetime.timedelta(days=8-date.isoweekday())
    return date