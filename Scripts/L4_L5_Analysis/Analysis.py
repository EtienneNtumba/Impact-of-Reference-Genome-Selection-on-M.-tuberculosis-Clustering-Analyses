import pandas as pd
from tools import ace_tools as tools

# Load the matrices from the files
matrix_L5_L5 = pd.read_csv('Matrix_L5_all.txt', sep='\t', header=None)
matrix_L5_L4 = pd.read_csv('Matrix_L4_all.txt', sep='\t', header=None)
matrix_L6_N1177 = pd.read_csv('Matrix_L6_mask_N1177-L6.txt', sep='\t', header=None)
matrix_L6_H37Rv = pd.read_csv('Matrix_L6_mask_H37Rv.txt', sep='\t', header=None)


#####         Flatten the matrices into single columns, excluding zeros
flatten_matrix_L5_L5 = matrix_L5_L5.values.flatten()
flatten_matrix_L5_L5 = flatten_matrix_L5_L5[flatten_matrix_L5_L5 != 0]

flatten_matrix_L5_L4 = matrix_L5_L4.values.flatten()
flatten_matrix_L5_L4 = flatten_matrix_L5_L4[flatten_matrix_L5_L4 != 0]

flatten_matrix_L6_N1177 = matrix_L6_N1177.values.flatten()
flatten_matrix_L6_N1177 = flatten_matrix_L6_N1177[flatten_matrix_L6_N1177 != 0]

flatten_matrix_L6_H37Rv = matrix_L6_H37Rv.values.flatten()
flatten_matrix_L6_H37Rv = flatten_matrix_L6_H37Rv[flatten_matrix_L6_H37Rv != 0]

# Create a DataFrame from the flattened arrays
combined_matrix_flat = pd.DataFrame({
    'Matrix_L5_refL5_mask_L5': pd.Series(flatten_matrix_L5_L5),
    'Matrix_L5_refL4_mask_L4': pd.Series(flatten_matrix_L5_L4),
    'Matrix_L6_refL6_mask_L6': pd.Series(flatten_matrix_L6_N1177),
    'Matrix_L6_refL6_mask_L4': pd.Series(flatten_matrix_L6_H37Rv)
})

from tools import ace_tools as tools

#tools.display_dataframe_to_user(name="Flattened Combined Matrix Data", dataframe=combined_matrix_flat)

import ace_tools as tools; tools.display_dataframe_to_user(name="Flattened Combined Matrix Data", dataframe=combined_matrix_flat)

combined_matrix_flat.head()

############################# Plot  ###################################################

import matplotlib.pyplot as plt

# Drop NaN values for boxplot
data_for_boxplot = combined_matrix_flat.dropna(axis=0, how='all')

# Plotting the boxplots for each column in the same figure
plt.figure(figsize=(12, 8))
data_for_boxplot.boxplot(column=[
    'Matrix_L5_refL5_mask_L5', 
    'Matrix_L5_refL4_mask_L4', 
    'Matrix_L6_mask_N1177_L6', 
    'Matrix_L6_mask_H37Rv'
])
plt.title('Boxplots of Non-zero Elements from Each Matrix')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

### ################################### Summary stat ###############################

# Calculate summary statistics for each column
summary_stats = combined_matrix_flat.describe()

# Transpose for better readability
summary_stats_transposed = summary_stats.T

tools.display_dataframe_to_user(name="Summary Statistics of Each Column", dataframe=summary_stats_transposed)

summary_stats_transposed


### To cut f1

##cut -d',' -f1 --complement Matrix_L5_all.csv
