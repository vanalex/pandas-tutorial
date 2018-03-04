import  header
import file_paths
import import_data as i_data
import matplotlib.pyplot as plt

# read csv
complaints = i_data.read_csv(file_paths.SERVICE_REQUESTS_FILE_PATH)

print(complaints)

# we need to get the complain as noise, so we need to filter as follows
noise_complaints = complaints[complaints['Complaint Type'] == 'Noise - Street/Sidewalk']
# print as a sample
print(noise_complaints[:3])

is_noise = complaints['Complaint Type'] == 'Noise - Street/Sidewalk'
is_brooklyn = complaints['Borough'] == 'BROOKLYN'
print('')
print(complaints[is_noise & is_brooklyn][:3])

print('')
print(complaints[is_noise & is_brooklyn][['Complaint Type', 'Borough','Created Date', 'Descriptor']][:10])

print('')
print('which borough has the most noise complaints?')
print(noise_complaints['Borough'].value_counts())

print('')
print('We want to divide by the total number of complaints, to make it make a bit more sense')
noise_complaints_count = noise_complaints['Borough'].value_counts()
complaints_counts = complaints['Borough'].value_counts()
print('noise rate: ')
print(noise_complaints_count / complaints_counts)
plot_information = noise_complaints_count / complaints_counts
plot_information.plot(kind='bar')
plt.show()


