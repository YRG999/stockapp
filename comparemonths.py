# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading the data
# data = pd.read_csv('AAPL_stock_data.csv')
data = pd.read_csv('SPY_stock_data.csv')

# Converting the 'Date' column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Extracting month, day of the month and year from Date
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month_name()
data['Day'] = data['Date'].dt.day

# Calculating the difference in closing price from the last closing price from the previous session
data['Close_diff'] = data['Close'].diff()

# Grouping data by month and day of the month and taking mean of closing price difference
monthly_data_day_diff = data.groupby(['Month', 'Day'], as_index=False).mean()

# Creating new plot
plt.figure(figsize=(14,7))

# Plotting each month's data
for month in monthly_data_day_diff['Month'].unique():
    monthly_data = monthly_data_day_diff[monthly_data_day_diff['Month'] == month]
    plt.plot(monthly_data['Day'], monthly_data['Close_diff'], label=month)

# plt.title('AAPL Stock Mean Daily Price Change by Day of Month')
plt.title('SPY Stock Mean Daily Price Change by Day of Month')
plt.xlabel('Day of Month')
plt.ylabel('Mean Daily Price Change ($)')
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1))
plt.grid(True)
plt.show()

# Counting the number of days the stock closed below the prior session's close
below_prior_close_days = data[data['Close_diff'] < 0].shape[0]

# Counting the number of days the stock closed above the prior session's close
above_prior_close_days = data[data['Close_diff'] > 0].shape[0]

# Counting the number of days the stock closed at the same price as the prior session's close
same_as_prior_close_days = data[data['Close_diff'] == 0].shape[0]

# Calculating the total number of days in the dataset
total_days = data.shape[0]

# Creating a DataFrame for the results
results = pd.DataFrame({
    'Closing Condition': ['Below Prior Close', 'Above Prior Close', 'Same as Prior Close', 'Total'],
    'Number of Days': [below_prior_close_days, above_prior_close_days, same_as_prior_close_days, total_days]
})

print(results)
