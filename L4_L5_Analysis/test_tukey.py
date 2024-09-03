import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import numpy as np

# Load the combined matrix data from the CSV file
file_path = 'Flattened_Combined_Matrix_Data.csv'
combined_matrix_flat = pd.read_csv(file_path)

# Prepare data for Tukey's HSD test
data = []
labels = []

for label, column in combined_matrix_flat.items():
    non_null_data = column.dropna().values
    data.extend(non_null_data)
    labels.extend([label] * len(non_null_data))

data = np.array(data)
labels = np.array(labels)

# Perform Tukey's HSD test
tukey_result = pairwise_tukeyhsd(endog=data, groups=labels, alpha=0.05)

print(tukey_result)
