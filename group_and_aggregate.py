import  header
import file_paths
import import_data as i_data
import matplotlib.pyplot as plt

bikes = i_data.read_csv(file_paths.BIKES_CSV_FILE_PATH)
print(bikes)

bikes['Berri 1'].plot()
plt.show()

berri_bikes = bikes[['Berri 1']].copy()
print('')
print(berri_bikes[:5])

# if we wanted to get the day of the month for each row, we could do it like this: berri_bikes.index.day

# These are the days of the week, where 0 is Monday. I found out that 0 was Monday by checking on a calendar.

# Now that we know how to get the weekday, we can add it as a column in our dataframe like this:

berri_bikes.loc[:, 'weekday'] = berri_bikes.index.weekday

print('')
print(berri_bikes[:5])

# Group the rows by weekday and then add up all the values with the same weekday.”
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
print('')
print(weekday_counts)

# we change the index
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print('')
print(weekday_counts)

# plot it
weekday_counts.plot(kind='bar')
plt.show()

