import pandas

data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()
# avg = sum(temp_list)/len(temp_list)
# print(avg)

# Average method for data
# print(data["temp"].mean())

# Max method for data
# print(data["temp"].max())

# Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
print(data[data.day == "Monday"])

# Challenge: print row of data which had the highest temperature
# print(data[data.temp == data.temp.max()])
#

print(data[data.day == "Monday"].condition)

# Convert Celsius to Fahrenheit of temp on Monday
# monday_temp = data[data.day == "Monday"]
# print(monday_temp.temp * 1.8 + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")