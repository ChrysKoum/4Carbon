import earthkit.data
import os
import numpy as np
from datetime import datetime, timedelta
import pandas as pd
# Get all .nc files in the current directory
nc_files = [f for f in os.listdir('.') if f.endswith('.nc')]

# Sort the files alphabetically
nc_files.sort()
# Initialize an empty list to store the values from each file
all_values = []
all_dates = []

# Set the start date
start_date = datetime(2020, 8, 26, 12, 0)


ds = earthkit.data.from_source("file", "bsecond.nc")
print(ds.metadata() )
#[NetCDFMetadata({'species': 'Carbon Monoxide', 'units': 'µg/m3', 'value': 'hourly values', 'standard_name': 'mass_concentration_of_carbon_monoxide_in_air', 'variable': 'co_conc', 'level': 0, 'levtype': 'level'}),
print(ds[0].shape)
print(ds[0].values)
print(ds[0].values.shape)
print(ds[0])
# print(ds[0].metadata())
# print(ds[0].metadata(["level", "variable"]))
# data_dict = {}
# for file in nc_files:
#     ds = earthkit.data.from_source("file", file)
#     for f in ds:
#         print(len(f.values))
#         print(f.metadata(["level", "variable"]))
#         import matplotlib.pyplot as plt

#         plt.figure(figsize=(10, 6))
#         plt.plot(f.values)
#         plt.title(f"Values for {f.metadata(['level', 'variable'])}")
#         plt.xlabel('Index')
#         plt.ylabel('Value')
#         plt.show()
#     break

# for f in ds:
    
#     key = f.metadata(["level", "variable"])
#     key = f"level_{key[0]}_variable_{key[1]}"
#     if key not in data_dict:
#         data_dict[key] = pd.DataFrame(columns=['datetime', 'values'])
        
#         # Append the new data to the DataFrame
#     new_data = pd.DataFrame({'datetime': [(start_date+timedelta(days=i)).strftime("%Y-%m-%d %H:%M") for i in range(len(f.values))], 'values': f.values.tolist()})
#     data_dict[key] = pd.concat([data_dict[key], new_data], ignore_index=True)

# print(data_dict)
# # v = ds[0].values
# v = ds.to_numpy()
# Initialize a dictionary to store DataFrames for each unique metadata combination
data_dict = {}

# Set the start date
start_date = datetime(2020, 8, 26, 12, 0)

# Iterate through all files in the dataset
for i, f in enumerate(nc_files):

    df = earthkit.data.from_source("file", f)

    for ds in df:
        # Get metadata
        key = ds.metadata(["level", "variable"])
        
        # Create a key from the metadata
        key = f"level_{key[0]}_variable_{key[1]}"
        
        # Calculate the date for this data point
        # current_date = start_date + timedelta(days=i)
        data = [sum(ds.values[i:i+4]) / 4 for i in range(0, len(ds.values), 4)]
        # If the key doesn't exist in the dictionary, create a new DataFrame
        if key not in data_dict:
            data_dict[key] = pd.DataFrame(columns=['datetime', 'values'])
        
        # Append the new data to the DataFrame
        new_data = pd.DataFrame({'datetime': [(start_date+timedelta(days=i)).strftime("%Y-%m-%d %H:%M") for i in range(len(ds.values))], 'values': data})
        data_dict[key] = pd.concat([data_dict[key], new_data], ignore_index=True)
    start_date = start_date + timedelta(days=len(ds.values)+1)

print(data_dict)

    # Append the new data to the DataFrame
# # Print the resulting dictionary of DataFrames
# for key, df in data_dict.items():
#     print(f"\nKey: {key}")
#     print(df)


# # # Iterate through the sorted .nc files
# # for i, file in enumerate(nc_files):
# #     ds = earthkit.data.from_source("file", file)
# #     # Get all variables from the dataset
# #     for variable in ds:
# #         all_values.append(variable.values)
    
# #     # Calculate the date for this data point
# #     current_date = start_date + timedelta(days=i)
# #     all_dates.append(current_date)

# # # Concatenate all values along the first axis (assuming this is the time dimension)
# # concatenated_values = np.concatenate(all_values, axis=0)

# # print(f"Shape of concatenated values: {concatenated_values.shape}")
# # print("Dates:")
# # for date in all_dates:
# #     print(date.strftime("%Y-%m-%d %H:%M"))
# # print("Concatenated values:")
# # print(concatenated_values)
