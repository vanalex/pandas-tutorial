import pandas as pd
import numpy as np

# read csv
complaints = pd.read_csv('./data/311-service-requests.csv')

# print table
print(complaints)

# fixing the nan values
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('./data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})
print('')
print(requests['Incident Zip'].unique())

rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
print('##################################################################')
print(requests[rows_with_dashes])
