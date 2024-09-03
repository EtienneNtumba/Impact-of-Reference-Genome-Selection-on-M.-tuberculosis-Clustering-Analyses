import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file, skipping the first row
file_path = 'Epi_L6_ref6_maskL6_matrix.txt'  # Replace with the correct path
data = pd.read_csv(file_path, sep='\t', skiprows=1, header=None)

# Plot histograms for data distribution for each column
num_columns = data.shape[1]

# Create subplots
if num_columns == 1:
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.hist(data.iloc[:, 0], bins=20, color='blue', edgecolor='black')
    ax.set_title('Distribution of Column 1')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
else:
    fig, axes = plt.subplots(nrows=num_columns, ncols=1, figsize=(10, num_columns*3))
    for i, column in enumerate(data.columns):
        axes[i].hist(data[column], bins=20, color='blue', edgecolor='black')
        axes[i].set_title(f'Distribution of Column {column+1}')
        axes[i].set_xlabel('Value')
        axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()
