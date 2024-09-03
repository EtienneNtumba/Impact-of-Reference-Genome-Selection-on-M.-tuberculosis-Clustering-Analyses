#I'll clean the data, generate summary statistics, perform the Shapiro-Wilk normality test, and create the box plot in separate steps.
#Step-by-Step Approach

 #   Load and clean the data.
  #  Generate summary statistics.
   # Perform the Shapiro-Wilk test.
    #Create the box plot.

import pandas as pd
import numpy as np

# Load the data from the uploaded files
file_path_1 = 'Matrice_L4_dists_refL6_Mask_L6_lower_triangular.csv'
file_path_2 = 'Matrice_L4_dists_refL4_Mask_L4_lower_triangular.csv'

# Read the data, ignoring the headers
data_1 = pd.read_csv(file_path_1, header=None, skiprows=1, usecols=range(1, 44))
data_2 = pd.read_csv(file_path_2, header=None, skiprows=1, usecols=range(1, 44))

# Flatten the data into a single list of values for both files
flattened_data_1 = data_1.values.flatten()
flattened_data_2 = data_2.values.flatten()

# Remove zeros and NaNs
cleaned_data_1 = flattened_data_1[~np.isnan(flattened_data_1)]
cleaned_data_1 = cleaned_data_1[cleaned_data_1 != 0]

cleaned_data_2 = flattened_data_2[~np.isnan(flattened_data_2)]
cleaned_data_2 = cleaned_data_2[cleaned_data_2 != 0]

# Convert to numeric type and drop NaNs again to ensure cleanliness
cleaned_data_1 = pd.Series(cleaned_data_1).dropna().astype(float)
cleaned_data_2 = pd.Series(cleaned_data_2).dropna().astype(float)

cleaned_data_1, cleaned_data_2

# Generate summary statistics
summary_statistics_1 = cleaned_data_1.describe()
summary_statistics_2 = cleaned_data_2.describe()

# Perform Shapiro-Wilk test for normality
from scipy.stats import shapiro
shapiro_test_1 = shapiro(cleaned_data_1)
shapiro_test_2 = shapiro(cleaned_data_2)

# Print results
print("Summary Statistics for Data 1:")
print(summary_statistics_1)
print("\nShapiro-Wilk Test for Data 1:")
print(shapiro_test_1)

print("\nSummary Statistics for Data 2:")
print(summary_statistics_2)
print("\nShapiro-Wilk Test for Data 2:")
print(shapiro_test_2)

import matplotlib.pyplot as plt

# Generate box plot for both datasets
plt.figure(figsize=(12, 8))
plt.boxplot([cleaned_data_1, cleaned_data_2], vert=False, patch_artist=True,
            boxprops=dict(facecolor="lightblue"), labels=["Data 1", "Data 2"])
plt.title("Box Plot Comparison of Two Datasets")
plt.xlabel("Values")
plt.show()



