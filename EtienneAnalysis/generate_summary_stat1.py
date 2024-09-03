import pandas as pd

# Load the data from the file, skipping the first row
file_path = 'Epi_L6_mask_H37Rv.txt'
data = pd.read_csv(file_path, sep='\t', skiprows=1, header=None)

# Calculate summary statistics for each column using all rows
summary_stats = data.describe().loc[['count', 'mean', 'std', 'min', 'max']]
summary_stats.loc['sum'] = data.sum()
summary_stats = summary_stats.rename(index={
    'count': 'Count',
    'mean': 'Mean',
    'std': 'Standard Deviation',
    'min': 'Min',
    'max': 'Max',
    'sum': 'Sum'
})

# Save summary statistics to DataFrame
summary_stats_df = pd.DataFrame(summary_stats)

# Display the summary statistics DataFrame
print(summary_stats_df)



