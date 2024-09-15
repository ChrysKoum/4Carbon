import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import matplotlib.dates as mdates

data= {
    'Month-Year': [
        'Jan-20', 'Feb-20', 'Mar-20', 'Apr-20', 'May-20', 'Jun-20', 'Jul-20', 'Aug-20', 'Sep-20', 'Oct-20', 'Nov-20', 'Dec-20',
        'Jan-21', 'Feb-21', 'Mar-21', 'Apr-21', 'May-21', 'Jun-21', 'Jul-21', 'Aug-21', 'Sep-21', 'Oct-21', 'Nov-21', 'Dec-21',
        'Jan-22', 'Feb-22', 'Mar-22', 'Apr-22', 'May-22', 'Jun-22', 'Jul-22', 'Aug-22', 'Sep-22', 'Oct-22', 'Nov-22', 'Dec-22',
        'Jan-23', 'Feb-23', 'Mar-23', 'Apr-23', 'May-23', 'Jun-23', 'Jul-23', 'Aug-23', 'Sep-23', 'Oct-23', 'Nov-23', 'Dec-23',
        'Jan-24'
    ],
    'Arrivals (in thousands)': [
        812, 900, 150, 200, 200, 500, 1400, 3000, 2000, 1500, 200, 180,
        147, 130, 100, 250, 400, 1200, 3000, 4500, 3700, 2100, 500, 450,
        432, 500, 600, 700, 2000, 3000, 5800, 6200, 4300, 2700, 1000, 750,
        726, 760, 900, 1400, 2000, 4000, 6000, 6500, 5000, 3200, 1100, 900,
        717  # Jan-24
    ]
}

df = pd.DataFrame(data)
# Extract the 'Arrivals (in thousands)' column
data = df['Arrivals (in thousands)'].values

# Create lagged data (12 months ago)
n_lag = 12
X = data[:-n_lag]  # Input features (same month last year)
y = data[n_lag:]   # Target values (current month)

# Shift the index accordingly
df_lagged = pd.DataFrame({'Previous Year': X, 'Current Year': y})


# Calculate the percentage change between each year for the same month
growth_rate = []

# We'll calculate the growth between the same months in consecutive years
for i in range(12, len(data)):
    prev_year_value = data[i - 12]  # Value from the same month last year
    current_value = data[i]
    growth_rate.append((current_value - prev_year_value) / prev_year_value)

# Calculate the average growth rate across all years
avg_growth_rate = np.mean(growth_rate) 
# print(f'Average Monthly Growth Rate: {avg_growth_rate * 100:.2f}%')


# Forecast the next 12 months by applying the growth rate to the last 12 months
forecast_growth = data[-n_lag:] * (1 + avg_growth_rate* 0.1)


# Convert the 'Month-Year' column to datetime
df['Month-Year'] = pd.to_datetime(df['Month-Year'], format='%b-%y')

# Set 'Month-Year' as the index
df.set_index('Month-Year', inplace=True)

# Create a date range for the forecast
forecast_dates = pd.date_range(start=df.index[-1] + pd.DateOffset(months=1), periods=12, freq='M')

# Plot the true values, predictions with growth, and forecast
plt.figure(figsize=(12, 6))

# Plot the true values
plt.plot(df.index, data, label="True Arrivals", color='blue')

# Plot the forecast
plt.plot(forecast_dates, forecast_growth, label="Forecasted Arrivals", color='green')

plt.title('Tourist Arrivals: True and Forecasted (with Growth Adjustment)')
plt.xlabel('Month-Year')
plt.ylabel('Arrivals (in thousands)')
plt.legend()
plt.grid(True)

# Customize x-axis ticks to show months
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right')


plt.tight_layout()
plt.show()

