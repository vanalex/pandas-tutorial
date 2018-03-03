import matplotlib.pyplot as plt
import  header
import file_paths
import import_data as i_data

# read csv
complaints = i_data.read_csv(file_paths.SERVICE_REQUESTS_FILE_PATH)

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
complaint_type_counts = complaints['Complaint Type'].value_counts()
print(complaint_type_counts)

print('')
print('complaints type top 10 ')
print(complaint_type_counts[:10])

# plot
complaint_type_counts[:10].plot(kind='bar')
plt.show()

