# @author   Lucas Cardoso de Medeiros
# @since    04/09/2023
# @version  1.0

"""You've learnt about all the core aspects of data exploration, data cleaning, and data visualization. Download,
unzip and open the notebook I've included for this assignment. You'll find an incredibly rich dataset from next
spaceflight that includes all the space missions since the beginning of the Space Race between the USA and the Soviet
Union in 1957! It has data on the mission status (success/failure), the cost of the mission, the number of launches
per country, and much, much more. There's so much we can learn from this dataset about the dominant organizations and
the trends over time. For example, Who launched the most missions in any given year? How has the cost of a space
mission varied over time? Which months are the most popular for launches? Have space missions gotten safer or has the
chance of failure remained unchanged? I'm sure that you'll discover many more questions that you can formulate and
answer with this dataset! Use it to practice what you learnt about creating various types of charts and
visualizations, from choropleth to sunburst charts to segmented bar charts and see if you can turn data into insight.
Good luck!"""

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import iso3166
from datetime import datetime, timedelta

pd.options.display.float_format = '{:,.2f}'.format  # Notebook presentation

df_data = pd.read_csv('mission_launches.csv')  # Load data

print(df_data.shape)

df_data.head()

print(f"Any NaN: {df_data.isna().values.any()}\nAny duplicated: {df_data.duplicated().values.any()}")

df_without_price = df_data.drop(columns=['Price'])
df_without_price.head()

renamed_df = df_without_price
renamed_df.Location = renamed_df.Location.str.replace("USA", "UNITED STATES OF AMERICA")
renamed_df.Location = renamed_df.Location.str.replace("Gran Canaria", "UNITED STATES OF AMERICA")
renamed_df.Location = renamed_df.Location.str.replace("Russia", "RUSSIAN FEDERATION")
renamed_df.Location = renamed_df.Location.str.replace("Barents Sea", "RUSSIAN FEDERATION")
renamed_df.Location = renamed_df.Location.str.replace("New Mexico", "UNITED STATES OF AMERICA")
renamed_df.Location = renamed_df.Location.str.replace("Yellow Sea", "CHINA")
renamed_df.Location = renamed_df.Location.str.replace("Shahrud Missile Test Site", "Iran")
renamed_df.Location = renamed_df.Location.str.replace("Pacific Ocean", "UNITED STATES OF AMERICA")
renamed_df.Location = renamed_df.Location.str.replace("Pacific Missile Range Facility", "UNITED STATES OF AMERICA")

df_country = renamed_df["Location"].str.split(",", expand=True).reset_index()
df_country[3] = df_country[3].str.lstrip(" ")

col_1 = df_country[1]
col_2 = df_country[2]
col_3 = df_country[3]
new_df = []
for one, two, three in zip(col_1, col_2, col_3):
    if three is None:
        three = two
    if three is None:
        three = one
    new_df.append(three)


country_iso = []
for country in new_df:
    country = country.lstrip(" ")
    if country == "Iran":
        country = "IRAN, ISLAMIC REPUBLIC OF"
    if country == "North Korea":
        country = "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"
    if country == "South Korea":
        country = "KOREA, REPUBLIC OF"
    try:
        country_iso.append(iso3166.countries_by_name[country.upper()][2])
    except KeyError:
        print(country)

df_without_price["Country_ISO"] = pd.DataFrame(country_iso)

choro_df_launches = df_without_price.groupby(["Country_ISO"], as_index=False).agg({"Detail": pd.Series.count})
choro_df_launches.rename(columns={"Detail": "Launch_Counts"}, inplace=True)
choro_df_launches.sort_values("Launch_Counts", ascending=False)

fig = px.choropleth(choro_df_launches,
                    locations="Country_ISO",
                    color="Launch_Counts",
                    color_continuous_scale="sunsetdark")
fig.show()
