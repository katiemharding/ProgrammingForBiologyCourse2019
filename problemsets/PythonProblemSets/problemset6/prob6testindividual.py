#! /usr/bin/env python3

with open('Python_06.seq.txt', 'r') as unk_seq:
	for rawline in unk_seq:
		line = rawline.rstrip() # remove white space at end
		gene_id, seq = line.split() # split on white space in the middle
		print(">", gene_id, "\treverse seq\n",seq, sep ="")

