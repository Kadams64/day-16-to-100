import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = data["temp"].mean()
# print(average)
#
# print(data["temp"].max())
#
# # # both of the following work identically, just different notations
# # print(data["condition"]) # like a dictionary
# # print(data.condition) # like an object
#
# #  get data in a row
# print(data[data.day == "Monday"]) # filtering by condition
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# farenheit = monday.temp[0] * 1.8 + 32
# print(farenheit)

# create a dataframe

#start with a python dictionary e.g.:
data_dict = {
    "students": ["Amy", "James", "Kelly"],
    "scores": [76, 56, 85]
}
data = pandas.DataFrame(data_dict)
# save the dataframe as a csv
data.to_csv("new_data.csv")