import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Charger les matrices
matrice_L4 = pd.read_csv('Matrice_L4_dists_refL4_Mask_L4_lower_triangular.csv')
matrice_L6 = pd.read_csv('Matrice_L4_dists_refL6_Mask_L6_lower_triangular.csv')

# Extraire les valeurs triangulaires inférieures non nulles en excluant les noms des échantillons
def extract_non_zero_lower_triangular(matrix):
    values = []
    for i in range(1, matrix.shape[0]):
        for j in range(i):
            value = matrix.iloc[i, j+1]  # +1 pour ignorer la première colonne (noms des échantillons)
            if value != 0:
                values.append(value)
    return values

L4_values = extract_non_zero_lower_triangular(matrice_L4)
L6_values = extract_non_zero_lower_triangular(matrice_L6)

# Assurer que les deux listes ont la même longueur en coupant la plus longue
min_length = min(len(L4_values), len(L6_values))
L4_values = L4_values[:min_length]
L6_values = L6_values[:min_length]

# Construire le DataFrame
data = pd.DataFrame({
    'L4_refL6_mask_L6': L4_values,
    'L6_refL6_maskL6': L6_values
})

# Créer des étiquettes pour chaque condition (0 pour L4_refL6_mask_L6, 1 pour L6_refL6_maskL6)
labels = [0] * min_length + [1] * min_length
data['labels'] = labels

# Diviser les données en ensembles d'entraînement et de test
X = data[['L4_refL6_mask_L6', 'L6_refL6_maskL6']]
y = data['labels']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialiser le modèle Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entraîner le modèle
rf_model.fit(X_train, y_train)

# Prédire sur l'ensemble de test
y_pred = rf_model.predict(X_test)

# Évaluer le modèle
print(classification_report(y_test, y_pred))
