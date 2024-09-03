import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import shapiro, levene, f_oneway, kruskal

# Load the matrices from the files
matrix_L5_L5 = pd.read_csv('Matrix_L5_all.txt', sep='\t', header=None)
matrix_L5_L4 = pd.read_csv('Matrix_L4_all.txt', sep='\t', header=None)
matrix_L6_N1177 = pd.read_csv('Matrix_L6_mask_N1177-L6.txt', sep='\t', header=None)
matrix_L6_H37Rv = pd.read_csv('Matrix_L6_mask_H37Rv.txt', sep='\t', header=None)

# Flatten the matrices into single columns, excluding zeros
def flatten_and_filter(matrix):
    flattened = matrix.values.flatten()
    return flattened[flattened != 0]

flatten_matrix_L5_L5 = flatten_and_filter(matrix_L5_L5)
flatten_matrix_L5_L4 = flatten_and_filter(matrix_L5_L4)
flatten_matrix_L6_N1177 = flatten_and_filter(matrix_L6_N1177)
flatten_matrix_L6_H37Rv = flatten_and_filter(matrix_L6_H37Rv)

# Create a DataFrame from the flattened arrays
combined_matrix_flat = pd.DataFrame({
    'Matrix_L5_refL5_mask_L5': pd.Series(flatten_matrix_L5_L5),
    'Matrix_L5_refL4_mask_L4': pd.Series(flatten_matrix_L5_L4),
    'Matrix_L6_mask_N1177_L6': pd.Series(flatten_matrix_L6_N1177),
    'Matrix_L6_mask_H37Rv': pd.Series(flatten_matrix_L6_H37Rv)
})

# Check normality with Q-Q plots and Shapiro-Wilk test
columns = ['Matrix_L5_refL5_mask_L5', 'Matrix_L5_refL4_mask_L4', 'Matrix_L6_mask_N1177_L6', 'Matrix_L6_mask_H37Rv']
print("Checking Normality:")
for column in columns:
    # Q-Q Plot
    plt.figure(figsize=(6, 4))
    stats.probplot(combined_matrix_flat[column].dropna(), dist="norm", plot=plt)
    plt.title(f'Q-Q Plot for {column}')
    plt.show()
    
    # Shapiro-Wilk Test
    stat, p = shapiro(combined_matrix_flat[column].dropna())
    print(f'Shapiro-Wilk Test for {column}: W-statistic={stat}, p-value={p}')

# Check homogeneity of variances with Levene's test
print("\nChecking Homogeneity of Variances:")
stat, p = levene(
    combined_matrix_flat['Matrix_L5_refL5_mask_L5'].dropna(),
    combined_matrix_flat['Matrix_L5_refL4_mask_L4'].dropna(),
    combined_matrix_flat['Matrix_L6_mask_N1177_L6'].dropna(),
    combined_matrix_flat['Matrix_L6_mask_H37Rv'].dropna()
)
print(f"Levene's Test: W-statistic={stat}, p-value={p}")

# Perform appropriate statistical test based on normality and variance homogeneity
if all(shapiro(combined_matrix_flat[col].dropna())[1] > 0.05 for col in columns) and p > 0.05:
    # If data is normal and variances are equal, perform ANOVA
    print("\nPerforming ANOVA:")
    f_statistic, p_value = f_oneway(
        combined_matrix_flat['Matrix_L5_refL5_mask_L5'].dropna(),
        combined_matrix_flat['Matrix_L5_refL4_mask_L4'].dropna(),
        combined_matrix_flat['Matrix_L6_mask_N1177_L6'].dropna(),
        combined_matrix_flat['Matrix_L6_mask_H37Rv'].dropna()
    )
    print(f"ANOVA F-statistic: {f_statistic}, p-value: {p_value}")
else:
    # If data is not normal or variances are not equal, perform Kruskal-Wallis H-test
    print("\nPerforming Kruskal-Wallis H-test:")
    h_statistic, p_value = kruskal(
        combined_matrix_flat['Matrix_L5_refL5_mask_L5'].dropna(),
        combined_matrix_flat['Matrix_L5_refL4_mask_L4'].dropna(),
        combined_matrix_flat['Matrix_L6_mask_N1177_L6'].dropna(),
        combined_matrix_flat['Matrix_L6_mask_H37Rv'].dropna()
    )
    print(f"Kruskal-Wallis H-statistic: {h_statistic}, p-value: {p_value}")

# Plotting the boxplots for each column
plt.figure(figsize=(12, 8))
combined_matrix_flat.dropna(axis=0, how='all').boxplot(column=columns)
plt.title('Boxplots of Non-zero Elements from Each Matrix')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.show()

# Calculate summary statistics for each column
summary_stats = combined_matrix_flat.describe().T

# Print summary statistics for inspection
print("\nSummary Statistics:")
print(summary_stats)
