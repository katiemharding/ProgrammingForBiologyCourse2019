#! /usr/bin/env python3
import sys
from Bio import SeqIO
from Bio.SeqUtils import GC
from statistics import mean

file_name = sys.argv[1]

geneLength = [] 
geneGC = []

for seq_record in SeqIO.parse(file_name, "fasta"):
	geneLength.append(len(seq_record))
	geneGC.append(GC(seq_record.seq))

print('seqeunce count:', len(geneLength))
print('total number of nucleotides:', sum(geneLength))
print('avg len:', round(sum(geneLength)/len(geneLength)))
print('shortest len:', min(geneLength))
print('longest len:', max(geneLength))
print('avg GC content:', round(sum(geneGC)/len(geneLength),2))
print('lowest GC content:', round(min(geneGC),2))
print('highest GC content:', round(max(geneGC),2))

