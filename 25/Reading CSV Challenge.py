# with open("C:/Users/janob/PycharmProjects/100DaysOfCode/25/weather-data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

import csv

with open("weather-data.csv") as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temp = row[1]
            temperatures.append(int(temp))
print(temperatures)
