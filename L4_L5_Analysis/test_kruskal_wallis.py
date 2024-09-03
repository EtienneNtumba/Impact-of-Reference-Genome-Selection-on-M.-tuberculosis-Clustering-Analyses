import pandas as pd
from scipy.stats import kruskal

# Load the combined matrix data from the CSV file
file_path = 'Flattened_Combined_Matrix_Data.csv'
combined_matrix_flat = pd.read_csv(file_path)

# Extract non-null values for each column
data_L5_L5 = combined_matrix_flat['Matrix_L5_refL5_mask_L5'].dropna().values
data_L5_L4 = combined_matrix_flat['Matrix_L5_refL4_mask_L4'].dropna().values
data_N1177_L6 = combined_matrix_flat['Matrix_L6_mask_N1177_L6'].dropna().values
data_H37Rv_L6 = combined_matrix_flat['Matrix_L6_mask_H37Rv'].dropna().values

# Perform the Kruskal-Wallis H-test
statistic, p_value = kruskal(data_L5_L5, data_L5_L4, data_N1177_L6, data_H37Rv_L6)

print(f"Kruskal-Wallis H-test statistic: {statistic}")
print(f"P-value: {p_value}")
