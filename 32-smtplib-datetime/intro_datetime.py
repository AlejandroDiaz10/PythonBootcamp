import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

weekday = now.weekday()
print(weekday)

dof = dt.datetime(year=2002, month=10, day=25, hour=17)
print(dof)
