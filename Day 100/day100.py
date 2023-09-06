# @author   Lucas Cardoso de Medeiros
# @since    05/09/2023
# @version  1.0

"""Extract insights from combining US census data and the Washington Post's database on deaths by police in the
United States.

Today you will do some deep analysis around an incredibly sensitive and politically charged topic. Since Jan. 1,
2015, The Washington Post has been compiling a database of every fatal shooting in the US by a police officer in the
line of duty. You will analyze this dataset together with US census data on poverty rate, high school graduation
rate, median household income, and racial demographics. This way we better understand social trends and what is going
on with the fatal use of force by the police in the United States."""

import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

pd.options.display.float_format = '{:,.2f}'.format

df_hh_income = pd.read_csv('Median_Household_Income_2015.csv', encoding="windows-1252")
df_pct_poverty = pd.read_csv('Pct_People_Below_Poverty_Level.csv', encoding="windows-1252")
df_pct_completed_hs = pd.read_csv('Pct_Over_25_Completed_High_School.csv', encoding="windows-1252")
df_share_race_city = pd.read_csv('Share_of_Race_By_City.csv', encoding="windows-1252")
df_fatalities = pd.read_csv('Deaths_by_Police_US.csv', encoding="windows-1252")

print(df_hh_income.shape)
print(df_pct_poverty.shape)
print(df_pct_completed_hs.shape)
print(df_share_race_city.shape)
print(df_fatalities.shape)

df_hh_income.head()

df_pct_poverty.head()

df_pct_completed_hs.head()

df_share_race_city.head()

df_fatalities.head()

print(f"Any NaN: {df_fatalities.isna().values.any()}\nAny duplicated: {df_fatalities.duplicated().values.any()}")

# converting date object into datetime
df_fatalities.date = pd.to_datetime(df_fatalities.date)

"""Number of Police Killings Over Time"""
killings_over_time = df_fatalities.groupby(['date', 'race'], as_index=False).state.count()
killings_over_time['year'] = killings_over_time['date'].dt.year
killings_over_time['month'] = killings_over_time['date'].dt.month
killings_over_time['Date'] = killings_over_time['date'].dt.day

killings_over_time = killings_over_time.groupby(['year', 'Date', 'race'], as_index=False).month.count()
killings_over_time.sort_values('Date', ascending=False)

# plotting graph
with sns.axes_style("whitegrid"):
    sns.lmplot(data=killings_over_time,
               x='month',
               y='Date',
               row='year',
               lowess=True,
               aspect=2,
               scatter_kws={'alpha': 0.6},
               line_kws={'color': 'black'})

"""How Old Were the People Killed?"""
armed_df = df_fatalities[df_fatalities.armed is True]

# separate KDE plot for each race
race_A = armed_df.loc[armed_df.race == "A"]
race_W = armed_df.loc[armed_df.race == "W"]
race_B = armed_df.loc[armed_df.race == "B"]
race_H = armed_df.loc[armed_df.race == "H"]
race_N = armed_df.loc[armed_df.race == "N"]
race_O = armed_df.loc[armed_df.race == "O"]

plt.figure(figsize=(8, 4), dpi=120)
with sns.axes_style("whitegrid"):
    sns.kdeplot(race_A.race.index, shade=True, color='#371B58')
    sns.kdeplot(race_W.race.index, shade=True, color='#810955')
    sns.kdeplot(race_B.race.index, shade=True, color='#18978F')
    sns.kdeplot(race_H.race.index, shade=True, color='#570A57')
    sns.kdeplot(race_N.race.index, shade=True, color='#0AA1DD')
    sns.kdeplot(race_O.race.index, shade=True, color='#F8CB2E')

plt.title("Distribution of Ages of the People Killed By Police")
plt.show()

"""Create a Bar Chart with Subsections Showing the Racial Makeup of Each US State"""
df_racial = df_share_race_city.groupby(['Geographic area'], as_index=False).agg(
    {
        'City': pd.Series.count,
        'share_hispanic': pd.Series.count,
        'share_asian': pd.Series.count,
        'share_native_american': pd.Series.count,
        'share_white': pd.Series.count,
        'share_black': pd.Series.count
    })

col_subset = ['share_hispanic', 'share_asian', 'share_native_american', 'share_white', 'share_black']

plt.figure(figsize=(16, 8), dpi=120)
fig = px.bar(df_racial,
             x='Geographic area',
             y=['share_hispanic', 'share_asian', 'share_native_american', 'share_white', 'share_black'],
             hover_name=df_racial['Geographic area'],
             title="Bar Chart with Subsections Showing the Racial Makeup of Each US State")
fig.update_layout(xaxis_title="Geographic area", yaxis_title="Racial Makeup")
fig.show()

"""Top 10 cities with the most police killings"""
df_fatalities_by_city = df_fatalities.groupby('city', as_index=False).agg({'id': pd.Series.count})
df_fatalities_by_city_10 = df_fatalities_by_city.sort_values('id', ascending=False).head(10)

df_fatalities_by_city_race = df_fatalities.groupby(['city', 'race'], as_index=False).agg({'id': pd.Series.count})
df_fatalities_by_city_race_10 = df_fatalities_by_city_race[
    df_fatalities_by_city_race.city.isin(df_fatalities_by_city_10.city)]

# Dataframe with share by race data for top 10 cities only
la = df_share_race_city[df_share_race_city.City == "Los Angeles city"]
st_louis = df_share_race_city[df_share_race_city.City == "St. Louis city"]
san_antonio = df_share_race_city[df_share_race_city.City == "San Antonio city"]
phoenix = df_share_race_city[df_share_race_city.City == "Phoenix city"]
miami = df_share_race_city[df_share_race_city.City == "Miami city"]
lv = df_share_race_city[df_share_race_city.City == "Las Vegas city"]
houston = df_share_race_city[df_share_race_city.City == "Houston city"]
columbus = df_share_race_city[df_share_race_city.City == "Columbus city"]
chicago = df_share_race_city[df_share_race_city.City == "Chicago city"]
austin = df_share_race_city[df_share_race_city.City == "Austin city"]

top_10_cities = pd.concat([la, st_louis, san_antonio, phoenix, miami, lv, houston, columbus, chicago, austin])
top_10_cities.head()

race_by_city_sums = top_10_cities.groupby('City').sum()
race_by_city_sums['total'] = race_by_city_sums.sum(axis=1)
race_by_city_sums.head()

# Get % of each race per city
race_by_city_pct = race_by_city_sums
race_by_city_pct.share_white = race_by_city_sums.share_white / race_by_city_sums.total
race_by_city_pct.share_black = race_by_city_sums.share_black / race_by_city_sums.total
race_by_city_pct.share_native_american = race_by_city_sums.share_native_american / race_by_city_sums.total
race_by_city_pct.share_asian = race_by_city_sums.share_asian / race_by_city_sums.total
race_by_city_pct.share_hispanic = race_by_city_sums.share_hispanic / race_by_city_sums.total

# Plot a histogram of race breakdown of police killings in the 10 cities
hist_cities_by_race = px.histogram(x=df_fatalities_by_city_race_10.id,
                                   y=df_fatalities_by_city_race_10.city,
                                   title='Top 10 Cities Where Police Killings Take Place, Broken Down by Race',
                                   hover_name=df_fatalities_by_city_race_10.race,
                                   color=df_fatalities_by_city_race_10.race,
                                   barnorm='percent')
hist_cities_by_race.update_layout(xaxis_title='Number of Fatalities',
                                  yaxis_title='City')
hist_cities_by_race.show()

# Contrast with population race breakdown in the same cities
bar2 = px.bar(race_by_city_pct,
              x=[
                  race_by_city_pct.share_white,
                  race_by_city_pct.share_black,
                  race_by_city_pct.share_native_american,
                  race_by_city_pct.share_asian,
                  race_by_city_pct.share_hispanic
              ],
              y=race_by_city_pct.index,
              title="Racial Makeup of US Cities that are the Top 10 Where Police Killings Take Place")
bar2.update_layout(xaxis_title='Racial Makeup (%)',
                   yaxis_title='City (Top 10 for Police Killings)',
                   coloraxis_showscale=False)
bar2.show()
