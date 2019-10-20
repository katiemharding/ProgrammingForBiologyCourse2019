#! /usr/bin/env python3
import sys

new_dna = sys.argv[1]

def reverse_dna(dna):
	with open(dna, "r") as unk_dna:
		dna = ''
		for rawline in unk_dna:
			line = rawline.rstrip()
			dna += line
		dna_fixed = dna.replace('\t', '')
		dna_rev = dna_fixed[::-1]
		return(dna_rev)

print(reverse_dna(new_dna))
