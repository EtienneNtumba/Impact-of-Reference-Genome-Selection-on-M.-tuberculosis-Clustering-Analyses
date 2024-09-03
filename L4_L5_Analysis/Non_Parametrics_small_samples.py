import pandas as pd
from scipy.stats import wilcoxon, mannwhitneyu
import numpy as np
from sklearn.utils import resample

# Charger les matrices
matrix_L5_L5 = pd.read_csv('Matrix_L5_all.txt', sep='\t', header=None)
matrix_L5_L4 = pd.read_csv('Matrix_L4_all.txt', sep='\t', header=None)
matrix_L6_N1177 = pd.read_csv('Matrix_L6_mask_N1177-L6.txt', sep='\t', header=None)
matrix_L6_H37Rv = pd.read_csv('Matrix_L6_mask_H37Rv.txt', sep='\t', header=None)

# Aplatir et filtrer les matrices pour exclure les zéros
def flatten_and_filter(matrix):
    flattened = matrix.values.flatten()
    return flattened[flattened != 0]

flatten_matrix_L5_L5 = flatten_and_filter(matrix_L5_L5)
flatten_matrix_L5_L4 = flatten_and_filter(matrix_L5_L4)
flatten_matrix_L6_N1177 = flatten_and_filter(matrix_L6_N1177)
flatten_matrix_L6_H37Rv = flatten_and_filter(matrix_L6_H37Rv)


#Test de Wilcoxon pour Échantillons Appariés

#Si vous avez des échantillons appariés, par exemple avant et après une certaine condition, vous pouvez utiliser le test de Wilcoxon.

# Exemple avec des données appariées entre L5_L5 et L5_L4
#stat, p_value = wilcoxon(flatten_matrix_L5_L5, flatten_matrix_L5_L4)
#print(f"Test de Wilcoxon (L5_L5 vs L5_L4): W-statistic={stat}, p-value={p_value}")


stat, p_value = wilcoxon(flatten_matrix_L6_N1177, flatten_matrix_L6_H37Rv)
print(f"Test de Wilcoxon (L6_N1177 vs L6_H37RV): W-statistic={stat}, p-value={p_value}")


#Test de Mann-Whitney U

#Pour comparer deux échantillons indépendants, par exemple L5_L5 vs L6_N1177.

# Exemple avec des données indépendantes entre L5_L5 et L6_N1177
stat, p_value = mannwhitneyu(flatten_matrix_L5_L5, flatten_matrix_L5_L4)
print(f"Test de Mann-Whitney U (L5_L5 vs L5_L4): U-statistic={stat}, p-value={p_value}")

#Test de Permutation

#Pour un test plus flexible qui ne repose pas sur des hypothèses strictes, vous pouvez utiliser un test de permutation. Ici, nous comparons L5_L5 et L6_H37Rv.

# Combiner les échantillons
combined = np.hstack((flatten_matrix_L5_L5, flatten_matrix_L6_H37Rv))

# Calculer la différence observée des médianes
obs_diff = np.median(flatten_matrix_L6_H37Rv) - np.median(flatten_matrix_L5_L5)

# Permutations
n_permutations = 10000
perm_diffs = []

for _ in range(n_permutations):
    permuted = resample(combined)
    perm_group1 = permuted[:len(flatten_matrix_L5_L5)]
    perm_group2 = permuted[len(flatten_matrix_L5_L5):]
    perm_diff = np.median(perm_group2) - np.median(perm_group1)
    perm_diffs.append(perm_diff)

p_value = np.mean(np.abs(perm_diffs) >= np.abs(obs_diff))
print(f"Test de permutation (L5_L5 vs L6_H37Rv): p-value={p_value}")
