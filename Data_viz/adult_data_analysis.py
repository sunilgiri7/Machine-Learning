import pandas as pd
import numpy as np

df = pd.read_csv('adult.csv')

# How many people of each race are represented in this dataset? This should be a Pandas
df['race'].value_counts()

# What is the average age of men?
df['age'].mean()

# What is the percentage of people who have a Bachelor's degree?
shape = df.shape[0]
degree_count = df['education'].value_counts()['Bachelors'] / shape * 100
degree_count

# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
advanced_degree = df['education'].value_counts()[['Bachelors', 'Masters', 'Doctorate']]
advanced_degree / shape * 100

# What percentage of people without advanced education make more than 50K?
total = len(df.index)
advanced = len(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Docotrate')].index)
without_advanced = total - advanced
without_advanced

# What is the minimum number of hours a person works per week?
min_work_hour = np.min(df['hours.per.week'])

# What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
total_hour = df['hours.per.week'].sum()
df.query('salary== ">50k" ')
work_hour_per = len(df[(df['hours.per.week'].min()) & (df['income'] == '>50k')])
work_hour_per / total_hour * 100

# What country has the highest percentage of people that earn >50K and what is that percentage?
df[(df['native.country'] == df['native.country']) & (df['income'] == '>50K')]

















