import pandas as pd

df = pd.read_csv('chicago.csv')
print(df.head())  # start by viewing the first few rows of the dataset!
df.columns
df.describe()
df.info()

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df[ 'Start Time' ])

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]
    
print('Most Frequent Start Hour:', popular_hour)