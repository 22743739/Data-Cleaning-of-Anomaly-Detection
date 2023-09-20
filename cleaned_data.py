import pandas as pd

# read the csv file into a dataframe
df = pd.read_csv("2023.04.05-13.34.10.csv")

# the columns we want to keep
columns_to_keep = [
    'System Time', 'System Uptime', 'Disk Size', 'Disk Free', 'Disk Usage', 'Connection Available',
    'Heading Target', 'Heading Actual', 'Speed Target', 'Speed Actual', 'Load Mass', 'Load Mass Is Stable',
    'Error Count', 'EVMS Error Code', 'EVMS Status Code', 'EVMS Amp Hours Remaining', 'EVMS Battery Voltage',
    'EVMS Temperature', 'Battery Percentage', 'Battery Current', 'BMS Detected Cells', 'BMS Detected Modules',
    'BMS Lowest Cell', 'BMS Highest Cell', 'BMS Average Cell', 'BMS Highest Temperature', 'BMS Lowest Temperature',
    'BMS Average Temperature', 'BMS Module 0 Balance Voltage', 'BMS Module 0 Cell 0', 'BMS Module 0 Cell 1',
    'BMS Module 0 Cell 2', 'BMS Module 0 Cell 3', 'BMS Module 0 Cell 4', 'BMS Module 0 Cell 5', 'BMS Module 0 Cell 6',
    'BMS Module 0 Cell 7', 'BMS Module 0 Cell 8', 'BMS Module 0 Detected Cells', 'BMS Module 0 Lowest Cell',
    'BMS Module 0 Highest Cell', 'BMS Module 0 Average Cell', 'BMS Module 0 Temperature', 'BMS Module 1 Balance Voltage',
    'BMS Module 1 Cell 0', 'BMS Module 1 Cell 1', 'BMS Module 1 Cell 2', 'BMS Module 1 Cell 3', 'BMS Module 1 Cell 4',
    'BMS Module 1 Cell 5', 'BMS Module 1 Cell 6', 'BMS Module 1 Cell 7', 'BMS Module 1 Cell 8', 'BMS Module 1 Detected Cells',
    'BMS Module 1 Lowest Cell', 'BMS Module 1 Highest Cell', 'BMS Module 1 Average Cell', 'BMS Module 1 Temperature',
    'BMS Module 2 Balance Voltage', 'BMS Module 2 Cell 0', 'BMS Module 2 Cell 1', 'BMS Module 2 Cell 2',
    'BMS Module 2 Cell 3', 'BMS Module 2 Cell 4', 'BMS Module 2 Cell 5', 'BMS Module 2 Cell 6', 'BMS Module 2 Cell 7',
    'BMS Module 2 Cell 8', 'BMS Module 2 Detected Cells', 'BMS Module 2 Lowest Cell', 'BMS Module 2 Highest Cell'
]

# Create a new DataFrame containing only the columns we want to keep
df_filtered = df[columns_to_keep]

# Delete lines containing non-values
df_filtered.dropna(inplace=True)

# Reset the index to ensure that the index is continuous
df_filtered.reset_index(drop=True, inplace=True)

print(df_filtered.head())

