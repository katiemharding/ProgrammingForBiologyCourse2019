#! /usr/bin/env python3
import sys

new_dna = sys.argv[1]

def calculate_perGC (dna):
	with open(dna, "r") as unk_dna:
		dna = ''
		for rawline in unk_dna:
			line = rawline.rstrip()
			dna += line
		dna_fixed = dna.replace('\t', '')
		c_count = dna_fixed.count('C')
		g_count = dna_fixed.count('G')
		dna_len = len( dna_fixed)
		gc_content = (c_count + g_count)/dna_len
		return(gc_content)

print(calculate_perGC(new_dna))
