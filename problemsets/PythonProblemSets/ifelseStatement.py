#!/usr/bin/env python3
import sys
short_sequence = "TTT"
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if short_sequence in dna:
	print(short_sequence + " is present")
else:
	print(short_sequence + " is not found")

