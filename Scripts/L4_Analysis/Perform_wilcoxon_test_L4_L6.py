import pandas as pd
from scipy.stats import wilcoxon

# Load the matrices
matrice_L4 = pd.read_csv('Matrice_L4_dists_refL4_Mask_L4_lower_triangular.csv')
matrice_L6 = pd.read_csv('Matrice_L4_dists_refL6_Mask_L6_lower_triangular.csv')

# Extract non-zero lower triangular values
def extract_non_zero_lower_triangular(matrix):
    values = []
    for i in range(1, matrix.shape[0]):
        for j in range(i):
            value = matrix.iloc[i, j+1]  # +1 to skip the first column (row names)
            if value != 0:
                values.append(value)
    return values

L4_values = extract_non_zero_lower_triangular(matrice_L4)
L6_values = extract_non_zero_lower_triangular(matrice_L6)

# Construct the dataframe
data = pd.DataFrame({
    'L4_refL6_mask_L6': L4_values,
    'L6_refL6_maskL6': L6_values
})

# Perform the Wilcoxon Signed-Rank Test
wilcoxon_test = wilcoxon(data['L4_refL6_mask_L6'], data['L6_refL6_maskL6'])
wilcoxon_test
