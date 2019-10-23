# /usr/bin/env python3

import sys
from Bio import SeqIO

file_name = sys.argv[1]

geneLength = [] 
geneGC = []

for seq_record in SeqIO.parse(file_name, "fasta"):
	geneLength.append(len(seq_record))

halfTotal = sum(geneLength)/2
contigLength = sorted(geneLength)
runningTotal = 0
N50 = 0
L50 = 0
for Length in contigLength:
	if runningTotal < halfTotal:
		runningTotal += Length
		L50 = Length
		N50 +=1
	else:
		break


print('seqeunce count:', len(geneLength))
print('total number of nucleotides:', sum(geneLength))
print(contigLength)
print('N50 = ', N50)
print('L50 = ', L50)
print('avg len:', round(sum(geneLength)/len(geneLength)))
print('shortest len:', min(geneLength))
print('longest len:', max(geneLength))
