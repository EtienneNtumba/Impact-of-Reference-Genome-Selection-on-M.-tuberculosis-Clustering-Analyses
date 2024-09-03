import sys,os

F = open(sys.argv[3],"wt")


for line1,line2 in zip(open(sys.argv[1]),open(sys.argv[2])):
	data = line1.split()
	datas = line2.split()
	F.write("\t".join(data+datas)+"\n")
#	print(data,datas)
