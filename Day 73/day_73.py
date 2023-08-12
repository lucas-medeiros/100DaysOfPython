# -*- coding: utf-8 -*-
"""Day 73.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1omgKjMFH-DryPoItVWHP0UQsR6XTFNNC

## Get the Data

Either use the provided .csv file or (optionally) get fresh (the freshest?) data from running an SQL query on StackExchange:

Follow this link to run the query from [StackExchange](https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com) to get your own .csv file

<code>
select dateadd(month, datediff(month, 0, q.CreationDate), 0) m, TagName, count(*)
from PostTags pt
join Posts q on q.Id=pt.PostId
join Tags t on t.Id=pt.TagId
where TagName in ('java','c','c++','python','c#','javascript','assembly','php','perl','ruby','visual basic','swift','r','object-c','scratch','go','swift','delphi')
and q.CreationDate < dateadd(month, datediff(month, 0, getdate()), 0)
group by dateadd(month, datediff(month, 0, q.CreationDate), 0), TagName
order by dateadd(month, datediff(month, 0, q.CreationDate), 0)
</code>

## Import Statements
"""

import pandas as pd
import matplotlib.pyplot as plt

"""## Data Exploration

**Challenge**: Read the .csv file and store it in a Pandas dataframe
"""

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.head()

"""**Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe"""

print(df.head())
print(df.tail())

"""**Challenge:** Check how many rows and how many columns there are.
What are the dimensions of the dataframe?
"""

print(f"df shape: {df.shape}")

"""**Challenge**: Count the number of entries in each column of the dataframe"""

df.count()

"""**Challenge**: Calculate the total number of post per language.
Which Programming language has had the highest total number of posts of all time?
"""

df.groupby('TAG').sum().sort_values('POSTS', ascending=False)

"""Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.

**Challenge**: How many months of data exist per language? Which language had the fewest months with an entry?

"""

df.groupby('TAG').count().sort_values('POSTS', ascending=False)

"""## Data Cleaning

Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"
"""

# Inspect data
print(df['DATE'][1])
print(df.DATE[1])

# Typeof column
print(type(df.DATE[1]))

# Convert entire column
df['DATE'] = pd.to_datetime(df['DATE'])
df['DATE']

"""## Data Manipulation


"""

# Test of .pivot() method

test_df = pd.DataFrame({'Age': ['Young', 'Young', 'Young', 'Young', 'Old', 'Old', 'Old'],
                        'Actor': ['Jack', 'Arnold', 'Keanu', 'Sylvester', 'Jack', 'Arnold', 'Keanu'],
                        'Power': [100, 80, 25, 50, 99, 75, 5]})
print(test_df)

pivoted_df = test_df.pivot(index='Age', columns='Actor', values='Power')
print(pivoted_df)

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.head()

"""**Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the column names and print out the first 5 rows of the dataframe."""

reshaped_df.shape

reshaped_df.columns

reshaped_df.head()

"""**Challenge**: Count the number of entries per programming language. Why might the number of entries be different?"""

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)

reshaped_df.isna().values.any()

"""## Data Visualisaton with with Matplotlib

**Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.
"""

plt.plot(reshaped_df.index, reshaped_df['java'])

plt.figure(figsize=(16,10))
plt.plot(reshaped_df.index, reshaped_df.java)

plt.figure(figsize=(16,8))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# plt.ylim(0, 25000)
plt.plot(reshaped_df.index, reshaped_df.java)

"""**Challenge**: Show two line (e.g. for Java and Python) on the same chart."""

plt.figure(figsize=(16,8))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# plt.plot(reshaped_df.index, reshaped_df.java, '-g', reshaped_df.index, reshaped_df.python, '-b')
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)

# Print all the programing langueges in the same chart

plt.figure(figsize=(16,8))
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 30000)
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], linewidth=2, label=reshaped_df[column].name)
plt.legend(fontsize=12)

"""# Smoothing out Time Series Data

Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move it forward by one overservation. Pandas has two handy methods already built in to work this out: [rolling()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html).
"""

# The window is number of observations that are averaged
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16,8))
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Posts', fontsize=12)
plt.ylim(0, 30000)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.ylim(0, 30000)

# plot the roll_df instead
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=2, label=roll_df[column].name)

plt.legend(fontsize=10)