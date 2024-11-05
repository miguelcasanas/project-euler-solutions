def is_leap_year(y):
    return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

def month_days(year, month):
    if month == 1: return 29 if is_leap_year(year) else 28
    if month > 6: month += 1
    return 30 if abs(month - 6) % 2 else 31

day, sundays = 1, 0
for year in range(1900, 2001):
    for month in range(12):
        if year >= 1901 and day % 7 == 0: sundays += 1
        day += month_days(year, month)

print(sundays)