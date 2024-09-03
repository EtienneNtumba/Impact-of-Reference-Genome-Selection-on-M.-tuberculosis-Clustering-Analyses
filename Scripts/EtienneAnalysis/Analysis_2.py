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
matrix_L6_N1177 = pd.read_csv('Epi_L6_ref6_maskL6_matrix.txt', sep='\t', header=None)
matrix_L6_H37Rv = pd.read_csv('Epi_L6_mask_H37Rv.txt', sep='\t', header=None)

# Flatten the matrices into single columns, excluding zeros
def flatten_and_filter(matrix):
    flattened = matrix.values.flatten()
    return flattened[flattened != 0]

#flatten_matrix_L5_L5 = flatten_and_filter(matrix_L5_L5)
#flatten_matrix_L5_L4 = flatten_and_filter(matrix_L5_L4)
flatten_matrix_L6_N1177 = flatten_and_filter(matrix_L6_N1177)
flatten_matrix_L6_H37Rv = flatten_and_filter(matrix_L6_H37Rv)

# Check the length of the flattened matrices to ensure they contain data
print("Length of flattened_matrix_L6_N1177:", len(flatten_matrix_L6_N1177))
print("Length of flattened_matrix_L6_H37Rv:", len(flatten_matrix_L6_H37Rv))

# Create a DataFrame from the flattened arrays
combined_matrix_flat = pd.DataFrame({
    'EPi_link_Matrix_L6_refL6_mask_L6': pd.Series(flatten_matrix_L6_N1177),
    'Epi_link_Matrix_L6_refL6_mask_H37Rv': pd.Series(flatten_matrix_L6_H37Rv)
})

# Check the columns of the DataFrame
print("Columns in the DataFrame:", combined_matrix_flat.columns)

# Display the combined DataFrame
try:
    tools.display_dataframe_to_user(name="Flattened Combined Matrix Data", dataframe=combined_matrix_flat)
except NameError:
    print("Display function from ace_tools is not available.")

# Plotting the boxplots for each column
plt.figure(figsize=(12, 8))
combined_matrix_flat.dropna(axis=0, how='all').boxplot(column=[
    'EPi_link_Matrix_L6_refL6_mask_L6', 
    'Epi_link_Matrix_L6_refL6_mask_H37Rv'
])
plt.title('Boxplots of Non-zero Elements from Each Matrix')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()
