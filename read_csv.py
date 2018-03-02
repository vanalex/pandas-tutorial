import pandas as pd
import matplotlib.pyplot as plt

# reading broken data
broken_df = pd.read_csv('./data/bikes.csv')
print(broken_df[:5])

# setting properties to fix the previous data
fixed_df = pd.read_csv('./data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True,
                       index_col='Date')
print(fixed_df[:5])

# select a column from data frame
selected_column = fixed_df['Berri 1']
print('print selected column')
print(selected_column)

# plotting the first column
# axis X are the months till november
# axis Y the value of the column Berri 1
fixed_df['Berri 1'].plot()
plt.show()

# plotting all the columns
fixed_df.plot(figsize=(15, 10))
plt.show()

