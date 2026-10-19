
#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sum_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
sum_gray = len(data[data["Primary Fur Color"] == "Gray"])
sum_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["Cinnamon", "Gray", "Black"],
    "Count": [sum_cinnamon, sum_gray, sum_black]
}

dataout = pandas.DataFrame(data_dict)
dataout.to_csv("squirrel_count_new.csv")







