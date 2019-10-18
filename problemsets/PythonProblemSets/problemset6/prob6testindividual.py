#! /usr/bin/env python3

genes = {}
gene_ID = "" 
seq = ""
with open('testhead.fasta', 'r') as unk_fasta:
	for rawline in unk_fasta:
		line = rawline.rstrip() # remove white space at end
		# line_list  = line.split(">") # split on white space in the middle
		if line[0] == '>':
			gene_ID =  line

		else:
			seq = line
			genes[gene_ID] = seq # because the gene and seq are called outside of the for loop
			# they are availabe to fill the genes dict here
print(genes)
# this is good because it loads in each line one at a time, keeping memory use low
	

