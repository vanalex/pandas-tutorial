import  header
import file_paths
import import_data as i_data
import matplotlib.pyplot as plt
import numpy as np

weather = i_data.read_csv(file_paths.WEATHER_FILE_PATH)
print(weather)

weather_description = weather['Weather']
print('')
print(weather_description)

is_snowing = weather_description.str.contains('Snow')
print(is_snowing[:5])
is_snowing = is_snowing.astype(float)
is_snowing.plot()
plt.show()