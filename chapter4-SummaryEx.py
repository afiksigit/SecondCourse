"""
Made by Afik
"""

def gen_secs():
    sec = 0
    while True:
        yield sec
        sec = (sec + 1) % 60


def gen_minutes():
    minute = 0
    while True:
        yield minute
        minute = (minute + 1) % 60


def gen_hours():
    hour = 0
    while True:
        yield hour
        hour = (hour + 1) % 24


def gen_time():
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)
                if sec == 59:
                    break
            if minute == 59:
                break
        if hour == 23:
            break


def gen_years(start=2023):
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    days = days_in_month[month]
    day = 1
    while day <= days:
        yield day
        day += 1


def gen_date():
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    date_gen = gen_date()
    for i in range(1, 10000000):
        date = next(date_gen)
        if i % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
