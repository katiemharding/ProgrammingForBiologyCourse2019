#! /usr/bin/env
import sys

File_Name = ''
try:
	File_Name = sys.argv[1]
	print("User provided file: ", File_Name)
except:
	print("Please provide Name")

genes = {}
gene_ID = ""
seq = ""
with open(File_Name, 'r') as unk_fasta:
	for rawline in unk_fasta:
		line = rawline.rstrip() # remove white space at end
	# line_list  = line.split(">") # split on white space in the middle
		if line[0] == '>':
			gene_info  =  line # now it needs cleanded up
			gene_long  = gene_info.replace('>','') # remove the identifer
			gene_ID = gene_long.split( ' ')[0] # remove everything after the tab
        # note: the above returns a two item list, one before \t one after \t
		else:
			seq = line
			genes[gene_ID] = seq # because the gene and seq are called outside of the for loop
        # they are availabe to fill the genes dict here
print(genes)
