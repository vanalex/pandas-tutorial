import pandas as pd
import matplotlib.pyplot as plt

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000)
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

# read csv
complaints = pd.read_csv('./data/311-service-requests.csv')

# print csv
# print(complaints) # uncomment to print

complaint_type = complaints['Complaint Type']
print('complaints type')
print(complaint_type)

print('print first 5 columns')
print(complaints[:5])

print('get first 5 rows of a column')
print(complaint_type[:5])

# print('we just want to know the complaint type and the borough, but not the rest of the information')
# print(complaints[['Complaint Type', 'Borough']])

print('That showed us a summary, and then we can look at the first 10 rows:')
print(complaints[['Complaint Type', 'Borough']][:10])

print('what is the most common complaint type?')
print(complaints['Complaint Type'].value_counts())