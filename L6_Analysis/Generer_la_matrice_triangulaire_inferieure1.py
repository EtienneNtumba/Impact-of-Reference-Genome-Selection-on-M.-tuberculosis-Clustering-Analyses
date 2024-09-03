import pandas as pd
import numpy as np
import argparse
import subprocess

# Configurer l'analyseur d'arguments
parser = argparse.ArgumentParser(description='Générer une matrice triangulaire inférieure à partir d\'un fichier CSV.')
parser.add_argument('--input', type=str, required=True, help='Chemin vers le fichier CSV d\'entrée')
parser.add_argument('--output', type=str, required=True, help='Chemin pour enregistrer le fichier CSV de sortie')

# Analyser les arguments
args = parser.parse_args()

# Définir une fonction pour générer la matrice triangulaire inférieure
def generate_lower_tri_matrix(input_file, output_file):
    # Lire le fichier CSV
    data = pd.read_csv(input_file, index_col=0)

    # Générer la matrice triangulaire inférieure en conservant les noms des échantillons
    lower_tri_matrix = data.where(np.tril(np.ones(data.shape)).astype(bool))

    # Enregistrer la matrice triangulaire inférieure résultante dans un nouveau fichier CSV
    lower_tri_matrix.to_csv(output_file)

    # Afficher les premières lignes de la matrice triangulaire inférieure résultante
    print(lower_tri_matrix.head())

# Exécuter la fonction avec les chemins de fichier d'entrée et de sortie fournis
generate_lower_tri_matrix(args.input, args.output)
