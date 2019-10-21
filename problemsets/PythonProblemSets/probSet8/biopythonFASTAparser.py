#! /usr/bin/env python3
import sys
from Bio import SeqIO
# from Bio.SeqUtils import GC

file_name = sys.argv[1]

for seq_record in SeqIO.parse(file_name, "fasta"):
	print(seq_record.id)
	print(len(seq_record))
#	print(GC(seq_record))


