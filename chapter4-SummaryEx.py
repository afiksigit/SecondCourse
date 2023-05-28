"""
Made by Afik
"""


def gen_secs():
    """
    Generator function that yields seconds from 0 to 59 indefinitely.
    """
    sec = 0
    while True:
        yield sec
        sec = (sec + 1) % 60


def gen_minutes():
    """
    Generator function that yields minutes from 0 to 59 indefinitely.
    """
    minute = 0
    while True:
        yield minute
        minute = (minute + 1) % 60


def gen_hours():
    """
    Generator function that yields hours from 0 to 23 indefinitely.
    """
    hour = 0
    while True:
        yield hour
        hour = (hour + 1) % 24


def gen_time():
    """
    Generator function that yields time in the format "HH:MM:SS" indefinitely.
    """
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
    """
    Generator function that yields years starting from the specified year indefinitely.

    :param start: The starting year. Default is 2023.
    """
    year = start
    while True:
        yield year
        year += 1


def gen_months():
    """
    Generator function that yields months from 1 to 12 indefinitely.
    """
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """
    Generator function that yields days of the specified month, considering leap year if specified.

    :param month: The month for which to generate days.
    :param leap_year: Boolean indicating whether to consider leap year. Default is True.
    """
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
    """
    Generator function that yields dates in the format "DD/MM/YYYY HH:MM:SS" indefinitely.
    """
    for year in gen_years():
        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    """
    The main function that generates and prints dates at regular intervals.
    """
    date_gen = gen_date()
    for i in range(1, 10000000):
        date = next(date_gen)
        if i % 1000000 == 0:
            print(date)


if __name__ == '__main__':
    main()
