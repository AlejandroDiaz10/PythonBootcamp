# Data: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")

fur_color_list = squirrel_data["Primary Fur Color"].unique().tolist()[1:]

# count_list = []
# for color in fur_color_list:
#     count = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
#     count_list.append(count)

count_list = [
    len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
    for color in fur_color_list
]

analysis = {"Fur Color": fur_color_list, "Count": count_list}

squirrel_analysis = pandas.DataFrame(analysis)
# squirrel_analysis.to_csv("squirrel_analysis.csv")
