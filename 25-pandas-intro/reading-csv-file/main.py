# ====================================================================
# "Default" way of reading a file. CSV files are a bit more complicated.
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# ====================================================================
# Option 1: Using the CSV module. Still a bit complicated.
# import csv
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# ====================================================================
# Option 2: Using the Pandas module. Much easier.
# import pandas

# data = pandas.read_csv("weather_data.csv")  # Dataframe (2D table)
# # print(data["temp"])  # Series (1D table)

# # Get data in columns
# print(data["temp"].mean())  # Compute average temperature
# print(data["temp"].max())  # Compute max temperature
# print(data["temp"].min())  # Compute min temperature

# print(data.temp.mean())  # Compute average temperature
# print(data.temp.max())  # Compute max temperature
# print(data.temp.min())  # Compute min temperature

# # Get data in rows
# print(data[data.day == "Monday"])  # Get data for Monday
# print(data[data["day"] == "Monday"])  # Get data for Monday

# print(data[data.temp == data.temp.max()])  # Get data for max temp day
# print(data[data["temp"] == data.temp.max()])  # Get data for max temp day

# print(data[data.day == "Monday"].temp * 9 / 5 + 32)  # Convert Monday temp to F

# ====================================================================
# Create a dataframe from scratch
import pandas

data = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data_frame = pandas.DataFrame(data)
print(data_frame)
data_frame.to_csv("new_data.csv")  # Save dataframe to csv file
