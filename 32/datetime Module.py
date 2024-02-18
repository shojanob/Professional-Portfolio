import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# if year == 2023:
#     print("This is true")

# print(now)
# print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=2003, month=5, day=6)
print(date_of_birth)