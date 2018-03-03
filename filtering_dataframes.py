import  header
import file_paths
import import_data as i_data

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
