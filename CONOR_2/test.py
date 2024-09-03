import sys,os


F =open("Text.txt","wt")


for line in open(sys.argv[1]):
	data = line.split(",")
	F.write("\t".join([data[0]])+"\n")
