#! /usr/bin/env
import sys
new_dna = sys.argv[1]
number = int(sys.argv[2])

# .strip() is only for the edges
# .replace() is for the middle
def cut_dna_to_pieces (dna, n):
	with open(dna, "r") as unk_dna:
		dna = ''
		for rawline in unk_dna:
			line = rawline.rstrip()
			dna += line
		dna_fixed = dna.replace('\t', '')
		for numb in range(0, len(dna_fixed), n):
			eachline = dna_fixed[numb:numb+n]
			print(eachline)

cut_dna_to_pieces(new_dna, number)
