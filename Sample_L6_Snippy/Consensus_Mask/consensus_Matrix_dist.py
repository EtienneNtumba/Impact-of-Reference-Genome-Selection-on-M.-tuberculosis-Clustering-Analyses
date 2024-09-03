from Bio import SeqIO
import Levenshtein as lev
import numpy as np
import sys
# Load sequences from a FASTA file
sequences = list(SeqIO.parse(sys.argv[1], "fasta"))

# Initialize an empty numpy array for the distance matrix
num_sequences = len(sequences)
distance_matrix = np.zeros((num_sequences, num_sequences))

# Calculate pairwise Levenshtein distances
for i in range(num_sequences):
    for j in range(i+1, num_sequences):
        dist = lev.distance(str(sequences[i].seq), str(sequences[j].seq))
        distance_matrix[i][j] = dist
        distance_matrix[j][i] = dist  # Symmetric matrix

# Optionally, convert the numpy array to a DataFrame for better readability
import pandas as pd
seq_ids = [seq.id for seq in sequences]
df = pd.DataFrame(distance_matrix, index=seq_ids, columns=seq_ids)
df.to_csv(sys.argv[2])
