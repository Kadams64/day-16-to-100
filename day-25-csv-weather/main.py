#
# with open("weather_data.csv", "r") as csv:
#     data = csv.readlines()
# print(data)

# import csv
#
# # I created a challenge for myself accidentally by naming this file
# # object "csv".  Renaming it to datafile worked much better
# with open("weather_data.csv", "r") as datafile:
#     data = csv.reader(datafile)
#     next(data) # skip the header row
#     temperatures = []
#     for row in data:
#         temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
column = data["temp"]
print(column)