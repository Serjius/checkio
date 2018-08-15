import calendar
#m, d, y = map(int, ('08 05 2015').split())
m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
