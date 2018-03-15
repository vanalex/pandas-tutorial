import pandas as pd
import numpy as np

# read csv
complaints = pd.read_csv('./data/311-service-requests.csv')

# this like print(complaints)
print(complaints.iloc[:][:])

# select the value of the first column and first row in different ways
print(complaints.iloc[0][0])
print(complaints.loc[0]['Unique Key'])
print(complaints.at[0,'Unique Key'])
print(complaints.iat[0,0])

# Use `iloc[]` to select row `0`
print(complaints.iloc[0])
# Use `loc[]` to select column 'Unique Key'
print(complaints.loc[:, 'Unique Key'])
