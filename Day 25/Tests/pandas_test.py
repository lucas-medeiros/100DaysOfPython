# @author   Lucas Cardoso de Medeiros
# @since    30/06/2022
# @version  1.0

# CSV files with Pandas lib


import pandas


FILE_PATH = "weather_data.csv"


# Reading CSV files with pandas
data = pandas.read_csv(FILE_PATH)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
print(data["temp"])

print(f"Average temperature for the week: {round(sum(temp_list) / len(temp_list), 2)}")
print(f"Average temperature for the week: {round(data['temp'].mean(), 2)}")

print(f"The max temperature for the week was: {data.temp.max()}")

# Get Data in columns
print(data["temp"])
print(data.temp)

# Get Data in rows
print(data[data.day == "Monday"])

# Get day when max temperature
print(data[data.temp == data.temp.max()])

# Get info from row
monday = data[data.day == "Monday"]
print("Monday condition")
print(monday.condition)

# Monday temp in F
print(f"Monday temp in F: {round((int(monday.temp) * 9/5) + 32, 2)}")

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
