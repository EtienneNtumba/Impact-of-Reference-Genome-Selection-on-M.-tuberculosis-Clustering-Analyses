import os,sys
import re


def extract_lineage(filename):
    with open(filename, 'r') as file:
        content = file.read()
        
        # Extract sample name (ID)
        id_match = re.search(r"ID:\s*(\S+)", content)
        sample_id = id_match.group(1) if id_match else "Unknown"
        
        # Extract lineage
        lineage_match = re.search(r"Strain:\s*(\S+)", content)
        lineage = lineage_match.group(1) if lineage_match else "Unknown"
        
        return sample_id, lineage

def main():
    with open(sys.argv[1], 'r') as samples_file:
        result_files = samples_file.read().splitlines()
    
    output_file = "lineage_summary.txt"
    
    with open(output_file, 'w') as out_file:
        out_file.write("Sample ID\tLineage\n")
        for result_file in result_files:
            if os.path.exists(result_file):
                sample_id, lineage = extract_lineage(result_file)
                out_file.write(f"{sample_id}\t{lineage}\n")
                print(f"Extracted {lineage} for {sample_id}")
            else:
                print(f"File {result_file} does not exist.")
                out_file.write(f"Unknown\tUnknown\n")

if __name__ == "__main__":
    main()
