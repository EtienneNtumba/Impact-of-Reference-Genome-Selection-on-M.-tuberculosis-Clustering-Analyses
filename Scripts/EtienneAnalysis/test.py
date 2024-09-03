import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the provided files
file1_path = 'Epi_L6_ref6_maskL6.txt'
file2_path = 'Epi_L6_mask_H37Rv.txt'

# Reading the data
data1 = pd.read_csv(file1_path, sep="\t", header=None)
data2 = pd.read_csv(file2_path, sep="\t", header=None)

# Cleaning and preparing the data for boxplot
# Removing the first row which contains headers in data1 and setting proper column names

# Split the first dataset's values by comma and remove the first row
data1_cleaned = data1.drop(0).iloc[:, 0].str.split(',', expand=True).iloc[:, 1:]
data1_cleaned.columns = ['Value1', 'Value2', 'Value3', 'Value4']
data1_cleaned = data1_cleaned.apply(pd.to_numeric)
data1_cleaned['Dataset'] = 'Epi_L6_ref6_maskL6'

# Processing the second file correctly
# Removing the header and converting the values to numeric
data2_cleaned = pd.DataFrame([int(line.strip()) for line in open(file2_path).readlines()[1:]], columns=['Value'])
data2_cleaned['Dataset'] = 'Epi_L6_mask_H37Rv'

# Combine the datasets for boxplotting
# First dataset: reshape to a long format
data1_long = pd.melt(data1_cleaned, id_vars=['Dataset'], value_vars=['Value1', 'Value2', 'Value3', 'Value4'], var_name='Metric', value_name='Value')

# Create the figure and subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# Boxplot for the first dataset (4 columns)
data1_long.boxplot(column='Value', by='Metric', ax=axs[0])
axs[0].set_title('Epi_L6_ref6_maskL6')
axs[0].set_xlabel('Metric')
axs[0].set_ylabel('Values')

# Boxplot for the second dataset (1 column)
data2_cleaned.boxplot(column='Value', by='Dataset', ax=axs[1])
axs[1].set_title('Epi_L6_mask_H37Rv')
axs[1].set_xlabel('Dataset')
axs[1].set_ylabel('Values')

# Adjust layout and display the plots
plt.suptitle('Boxplots of Two Datasets')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
