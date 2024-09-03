import pandas as pd
import matplotlib.pyplot as plt
import sys

# Load the data from the file, skipping the first row
#file_path = 'Epi_L6_mask_H37Rv.txt'  # Replace with the correct path
file_path = sys.argv[1]
data = pd.read_csv(file_path, sep='\t', skiprows=1, header=None)

# Calculate summary statistics for each column using all rows
summary_stats = data.describe().loc[['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']]
summary_stats.loc['sum'] = data.sum()
summary_stats = summary_stats.rename(index={
    'count': 'Count',
    'mean': 'Mean',
    'std': 'Standard Deviation',
    'min': 'Min',
    '25%': '25%',
    '50%': 'Median',
    '75%': '75%',
    'max': 'Max',
    'sum': 'Sum'
})

# Save summary statistics to DataFrame
summary_stats_df = pd.DataFrame(summary_stats)

# Display the summary statistics DataFrame
print("Summary Statistics:\n", summary_stats_df)

# Plot boxplots for data distribution for each column
plt.figure(figsize=(10, 6))
data.boxplot()
plt.title('Boxplot of Data Distribution')
plt.xlabel('Columns')
plt.ylabel('Values')
plt.show()
