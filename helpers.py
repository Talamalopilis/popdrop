import datetime

weekdays = {
    'm': 0,
    't': 1,
    'w': 2,
    'th': 3,
    'f': 4,
    's': 5,
    'su': 6
}


def get_session_date(day):
    val = weekdays[day]
    d = datetime.date.today()
    while d.weekday() != val:
        d += datetime.timedelta(days=1)
    return d