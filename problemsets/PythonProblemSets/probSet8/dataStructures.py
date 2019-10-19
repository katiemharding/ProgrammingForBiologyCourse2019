#! /usr/bin/env
import sys

File_Name = ''
try:
	File_Name = sys.argv[1]
	print("User provided file: ", File_Name)
except:
	print("Please provide Name")

genes = {}
gene_ID = None
with open(File_Name, 'r') as unk_fasta:
	for rawline in unk_fasta:
		line = rawline.rstrip() # remove white space at end
	# line_list  = line.split(">") # split on white space in the middle
		if line.startswith( '>'):
			gene_info  =  line # now it needs cleanded up
			gene_long  = gene_info.replace('>','') # remove the identifer
			gene_ID = gene_long.split( ' ')[0] # remove everything after the space
		# note: the above returns a multi item list, one before space one after space
			genes[gene_ID] = {} 
		# the above line set an empty vlaue, and starts the next sequence
		else:
			for nt in line: 
				if nt in genes[gene_ID]:
					previous_count =  genes[gene_ID][nt]
					new_count = previous_count +1
					genes[gene_ID][nt] = new_count
				else:
					genes[gene_ID][nt] = 1
			# this concatinates lines until the next > symbol is found
print(genes)
