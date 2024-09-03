import pandas as pd
import matplotlib.pyplot as plt
import sys

# Add the path to ace_tools module if necessary
# sys.path.append('/path/to/ACE_TOOLS')

# Import the ace_tools module
try:
    import ace_tools as tools
except ModuleNotFoundError:
    print("Error: ace_tools module not found. Please ensure it's installed and accessible.")

# Load the matrices from the files
#matrix_L5_L5 = pd.read_csv('Matrix_L5_all.txt', sep='\t', header=None)
#matrix_L5_L4 = pd.read_csv('Matrix_L4_all.txt', sep='\t', header=None)
matrix_L6_N1177 = pd.read_csv('Matrix_L6_mask_N1177-L6.txt', sep='\t', header=None)
matrix_L6_H37Rv = pd.read_csv('Matrix_L6_mask_H37Rv.txt', sep='\t', header=None)

# Flatten the matrices into single columns, excluding zeros
def flatten_and_filter(matrix):
    flattened = matrix.values.flatten()
    return flattened[flattened != 0]

#flatten_matrix_L5_L5 = flatten_and_filter(matrix_L5_L5)
#flatten_matrix_L5_L4 = flatten_and_filter(matrix_L5_L4)
flatten_matrix_L6_N1177 = flatten_and_filter(matrix_L6_N1177)
flatten_matrix_L6_H37Rv = flatten_and_filter(matrix_L6_H37Rv)

# Create a DataFrame from the flattened arrays
combined_matrix_flat = pd.DataFrame({
#    'Matrix_L5_refL5_mask_L5': pd.Series(flatten_matrix_L5_L5),
#    'Matrix_L5_refL4_mask_L4': pd.Series(flatten_matrix_L5_L4),
    'Matrix_L6_refL6_mask_L6': pd.Series(flatten_matrix_L6_N1177),
    'Matrix_L6_refL4_mask_L4': pd.Series(flatten_matrix_L6_H37Rv)
})

# Display the combined DataFrame
try:
    tools.display_dataframe_to_user(name="Flattened Combined Matrix Data", dataframe=combined_matrix_flat)
except NameError:
    print("Display function from ace_tools is not available.")

# Plotting the boxplots for each column
plt.figure(figsize=(12, 8))
combined_matrix_flat.dropna(axis=0, how='all').boxplot(column=[
   # 'Matrix_L5_refL5_mask_L5', 
   # 'Matrix_L5_refL4_mask_L4', 
    'Matrix_L6_refL6_mask_L6', 
    'Matrix_L6_refL4_mask_L4'
])
plt.title('Boxplots of Non-zero Elements from Each Matrix')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# Calculate summary statistics for each column
summary_stats = combined_matrix_flat.describe().T

# Display summary statistics
try:
    tools.display_dataframe_to_user(name="Summary Statistics of Each Column", dataframe=summary_stats)
except NameError:
    print("Display function from ace_tools is not available.")

# Print summary statistics for inspection
print(summary_stats)
