import sys,os


F = open(sys.argv[2],"wt")


for line in open(sys.argv[1]):
	data =line.split()
	if data[0].startswith("#"):
		F.write("\t".join(data)+"\n")
	else:
		if data[6]=='PASS':
			F.write('\t'.join(data[:5]+["."]+data[6:])+"\n")
		else:
			F.write('\t'.join(data[:5]+[".","."]+data[7:])+"\n")
