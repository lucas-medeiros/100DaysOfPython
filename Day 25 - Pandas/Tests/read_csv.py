# @author   Lucas Cardoso de Medeiros
# @since    30/06/2022
# @version  1.0

# Read CSV files


import csv
import pandas_test


FILE_PATH = "weather_data.csv"
DAY = "day"
TEMP = "temp"
CONDITION = "condition"
dataset = []
temperatures = []

# Reading CSV files with no libs
with open(file=FILE_PATH, mode="r") as file:
    data = file.readlines()
    for line in data[1:]:
        entry = {}
        info = line.split(',')
        entry[DAY] = info[0]
        entry[TEMP] = info[1]
        entry[CONDITION] = info[2].strip()
        dataset.append(entry)
    # print(dataset)


# Reading CSV files with csv lib
with open(file=FILE_PATH, mode="r") as file:
    data = csv.reader(file)
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)


# Reading CSV files with pandas
data = pandas.read_csv(FILE_PATH)
print(data["temp"])
