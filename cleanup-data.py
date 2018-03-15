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

# requests['Incident Zip'][rows_with_dashes] = np.nan

long_zip_codes = requests['Incident Zip'].str.len() > 5
requests['Incident Zip'][long_zip_codes].unique()
print('')
print(requests['Incident Zip'][long_zip_codes].unique())

print('')
requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)
print(requests['Incident Zip'])

print('')
print(requests[requests['Incident Zip'] == '00000'])

zero_zips = requests['Incident Zip'] == '00000'
requests['Incident Zip'][zero_zips] = np.nan

unique_zips = requests['Incident Zip'].unique()
print('')
print(unique_zips.sort())
print(unique_zips)