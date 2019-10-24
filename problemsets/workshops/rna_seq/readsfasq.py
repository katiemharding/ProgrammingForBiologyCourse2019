#! /usr/bin/env python3

import sys

file_name = sys.argv[1]
from Bio import SeqIO

sequences = []

for seq_record in SeqIO.parse(file_name, "fastq"):
	sequences.append(seq_record.seq)

print(sequences)

