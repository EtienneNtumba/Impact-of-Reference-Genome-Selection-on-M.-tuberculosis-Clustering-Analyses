from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input file for reading
with open(input_file, "r") as input_handle:
	sequences = list(SeqIO.parse(input_handle, "fasta"))

# Add necessary annotations, including molecule_type
for seq in sequences:
	seq.annotations["molecule_type"] = "DNA"

# Open the output file for writing
with open(output_file, "w") as output_handle:
	count = SeqIO.write(sequences, output_handle, "genbank")

print(f"Converted {count} records")
