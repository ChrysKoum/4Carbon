import netCDF4 as nc
import numpy as np
import os
import netCDF4 as nc
import pandas as pd
from datetime import datetime, timedelta

nc_files = [f for f in os.listdir('.') if f.endswith('.nc')]

# Sort the files alphabetically
nc_files.sort()
# Load the netCDF file
# file_path = 'afirst.nc'
# dataset = nc.Dataset(file_path)

# # Retrieve metadata and variable names
# metadata = dataset.__dict__
# variables = list(dataset.variables.keys())

# print("Metadata:", metadata)
# print("Variables:", variables)

# # Access a specific variable
# for var in variables:
#     data = dataset.variables[var][:]
#     print(f"Data for variable {var}:", data)




# # List of relevant pollutant variables
# pollutant_variables = ['co_conc', 'no2_conc', 'no_conc', 'o3_conc', 'pmwf_conc', 'so2_conc']

# # Dictionary to store the mean concentration data
# mean_concentrations = {}

# # Loop over each pollutant variable to calculate the mean across the grid
# for pollutant in pollutant_variables:
#     # Extract the pollutant data from the dataset
#     pollutant_data = dataset.variables[pollutant][:]
    
#     # Calculate the mean across the grid (latitude and longitude dimensions)
#     mean_pollutant_conc = np.mean(pollutant_data, axis=(2, 3))  # Mean over latitude and longitude
    
#     # Store the result in the dictionary
#     mean_concentrations[pollutant] = mean_pollutant_conc

#     print(f"Mean concentrations for {pollutant}:")
#     print(mean_pollutant_conc)

# # Close the dataset after usage
# dataset.close()



# Initialize the dictionary to hold data
data_dict = {}

# Set the start date
start_date = datetime(2020, 8, 26, 12, 0)

# Iterate through all files in the dataset
for f in nc_files:
    # Open the netCDF file
    dataset = nc.Dataset(f)

    # Iterate over pollutant variables
    pollutant_variables = ['o3_conc', 'pmwf_conc']#, 'so2_conc','co_conc', 'no2_conc', 'no_conc'

    for var in pollutant_variables:
        # Extract the pollutant data
        pollutant_data = dataset.variables[var][:]
        
        # Extract metadata for level
        levels = dataset.variables['level'][:]
        
        # Iterate through levels and add data to the dictionary
        #for i, level in enumerate(levels):
        # Create a key using the level and variable
        key = f"all_levels_variable_{var}"

        # If the key doesn't exist in the dictionary, create a new DataFrame
        if key not in data_dict:
            data_dict[key] = pd.DataFrame(columns=['datetime', 'values'])

        # Flatten the pollutant data for this level
        #pollutant_level_data = pollutant_data[:, i, :, :].mean(axis=(1, 2))  # Mean across latitude and longitude
        grid_mean_pollutant_conc = np.mean(pollutant_data, axis=(2, 3))  # Mean across lat and lon
        
        # Step 2: Take the mean across the levels (axis 1)
        pollutant_level_data = np.mean(grid_mean_pollutant_conc, axis=1)

        # Calculate monthly averages (every 30 values)
        monthly_values = [pollutant_level_data[j:j+30].mean() for j in range(0, len(pollutant_level_data), 30)]
        monthly_dates = [start_date + timedelta(days=30*j) for j in range(len(monthly_values))]

        # Append the new data to the DataFrame
        new_data = pd.DataFrame({
            'datetime': [date.strftime("%Y-%m-%d %H:%M") for date in monthly_dates],
            'values': monthly_values
            # 'datetime': [(start_date+timedelta(days=i)).strftime("%Y-%m-%d %H:%M") for i in range(pollutant_level_data.shape[0])],
            # 'values': pollutant_level_data.tolist()
        })
        data_dict[key] = pd.concat([data_dict[key], new_data], ignore_index=True)
    #start_date = start_date + timedelta(days=pollutant_level_data.shape[0]+1)
    start_date = monthly_dates[-1] + timedelta(days=30)
    # Close the dataset after processing
    dataset.close()

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Create a figure with subplots for each dataframe in the dictionary
num_plots = len(data_dict)
fig, axs = plt.subplots(num_plots, 1, figsize=(15, 5*num_plots), sharex=True)

# If there's only one plot, axs will be a single axis, not an array
if num_plots == 1:
    axs = [axs]

for i, (key, df) in enumerate(data_dict.items()):
    # Convert datetime column to datetime objects if it's not already
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    # Plot the data
    axs[i].plot(df['datetime'], df['values'])
    
    # Set the title for each subplot
    axs[i].set_title(key)
    
    # Set y-label
    axs[i].set_ylabel('Values')
    
    # Format x-axis
    axs[i].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    axs[i].xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    
    # Rotate and align the tick labels so they look better
    plt.setp(axs[i].xaxis.get_majorticklabels(), rotation=45, ha='right')

# Set a common xlabel for all subplots
fig.text(0.5, 0.04, 'Date', ha='center')

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()

# Now `data_dict` holds the time series data for each level and pollutant
