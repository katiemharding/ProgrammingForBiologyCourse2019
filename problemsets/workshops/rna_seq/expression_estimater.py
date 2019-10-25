#! usr/bin/env

import sys
import datetime

# the user needt to add a file name. make sure they do.
if len(sys.argv) < 2:
	print("please add file name")
	exit(1)

# add dates to log file
now = str(datetime.datetime.now())
now = now[:16] # cut down to date and time

print('# the program and datafile:',' '.join(sys.argv))
print('# was run on ', now)

file_name = sys.argv[1]

def main():
	gene_dict = {} 
	with open(file_name, 'r') as sam_file:
		for line in sam_file:
			line = line.rstrip() # remove whitespace at end
			line_list  = line.split("\t") # split on tab deliminater
			read_name = line_list[0] # first is read name
			gene_info = line_list[2] # third is gene info, need to divide on ^
			gene_name = gene_info.split('^')[0] # this is only gene name, not the transcript
			if gene_name not in gene_dict:
				gene_dict[gene_name] = set()
			gene_dict[gene_name].add(read_name)
# if not, in dictionary, then add gene name and empty set.  then add readname to set
	genes = list(gene_dict.keys())
	# make a list of the keys
	genes =  sorted(genes, key= lambda x: len(gene_dict[x]), reverse =True)

	for gene in genes:
		read_set = gene_dict[gene]
		print("{}\t{}".format(gene, len(read_set)))

	sys.exit(0)


if __name__ == '__main__':
	main()
