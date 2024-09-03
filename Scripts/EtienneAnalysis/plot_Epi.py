import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Epi_Table.txt'
data = pd.read_csv(file_path, sep="\t", header=None)
data.columns = ['Column1', 'Column2']

# Create subplots
fig, axs = plt.subplots(1, 1, figsize=(15, 12))

# Boxplot
axs[0, 0].boxplot([data['Column1'], data['Column2']], labels=['Column1', 'Column2'])
axs[0, 0].set_title('Boxplot')

# Histogram
#axs[0, 1].hist(data['Column1'], bins=10, alpha=0.5, label='Column1')
#axs[0, 1].hist(data['Column2'], bins=10, alpha=0.5, label='Column2')
#axs[0, 1].set_title('Histogram')
#axs[0, 1].legend()

# Scatter plot
#axs[1, 0].scatter(data['Column1'], data['Column2'])
#axs[1, 0].set_title('Scatter plot')
#axs[1, 0].set_xlabel('Column1')
#axs[1, 0].set_ylabel('Column2')

# Violin plot
#sns.violinplot(data=data, ax=axs[1, 1])
#axs[1, 1].set_title('Violin plot')

# Adjust layout
plt.tight_layout()
plt.show()
