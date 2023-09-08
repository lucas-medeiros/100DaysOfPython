# @author   Lucas Cardoso de Medeiros
# @since    30/06/2022
# @version  1.0

# Squirrel analysis files


import pandas


FILE_PATH = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
COLOR_COLUMN = "Primary Fur Color"


# Reading CSV files with pandas
data = pandas.read_csv(FILE_PATH)
gray, red, black = 0, 0, 0
result = {
    "Fur Color": ["gray", "red", "black"],
    "Count": []
}

for row in data[COLOR_COLUMN]:
    if row == "Gray":
        gray += 1
    elif row == "Cinnamon":
        red += 1
    elif row == "Black":
        black += 1

result["Count"] = [gray, red, black]
color_data = pandas.DataFrame(result)
color_data.to_csv("squirrel_count.csv")
print(color_data)
