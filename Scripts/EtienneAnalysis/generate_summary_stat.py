#!/bin/bash

# File paths
input_file="Epi_L6_mask_H37Rv.txt"
temp_file="selected_columns.tsv"
output_file="selected_rows_and_columns.tsv"

# Exclude the first column and keep the rest
cut --complement -f1 "$input_file" > "$temp_file"

# Select specific rows (2nd, 4th, and 6th)
awk 'NR==2 || NR==4 || NR==6' "$temp_file" > "$output_file"

# Calculate summary statistics
count=$(awk 'END {print NR}' "$output_file")
sum=$(awk '{s+=$1} END {print s}' "$output_file")
mean=$(awk '{s+=$1} END {print s/NR}' "$output_file")
stddev=$(awk '{x[NR]=$1; s+=$1} END {for (i=1;i<=NR;i++){sum_sq+=(x[i]-(s/NR))**2} print sqrt(sum_sq/NR)}' "$output_file")
min=$(awk 'NR==1{s=$1} $1<s{s=$1} END {print s}' "$output_file")
max=$(awk 'NR==1{s=$1} $1>s{s=$1} END {print s}' "$output_file")

# Print summary statistics
echo "Count: $count"
echo "Sum: $sum"
echo "Mean: $mean"
echo "Standard Deviation: $stddev"
echo "Min: $min"
echo "Max: $max"
