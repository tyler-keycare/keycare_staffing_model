import numpy as np
import pandas as pd
from scipy.stats import poisson

prov_count = 3

# Define the file path for raw visit length and charting time data
file_path = r'C:\Users\TylerMueller\Development\staffing_model\visit_charting_time.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Extract values from the specified columns
visit_lengths = df['VISIT_LENGTH_MINUTES'].tolist()
charting_lengths = df['PROV_TIME_TO_CLOSE_CHART'].tolist()


# get mean and st dev of each
mean_visit_length = np.mean(visit_lengths)
std_visit_length = np.std(visit_lengths)

mean_charting_length = np.mean(charting_lengths)
std_charting_length = np.std(charting_lengths)

# create variable based on distribution
visit_length_variable = np.random.normal(mean_visit_length, std_visit_length,1)
charting_length_variable = np.random.normal(mean_charting_length, std_charting_length,1)

# Clip the values to ensure they are within the desired range (0 to 20-30 minutes)
visit_length_variable = np.clip(visit_length_variable, 0, 30)
charting_length_variable = np.clip(charting_length_variable, 0, 20)

# Rounding to one decimal place
visit_length_variable = np.round(visit_length_variable, 1)
charting_length_variable = np.round(charting_length_variable, 1)

# print(charting_lengths[:20])

# Example usage
print(visit_length_variable)
print(charting_length_variable)

