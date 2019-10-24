#! /usr/bin/env python3

import sys

sequence = sys.argv[1]
number = int(sys.argv[2])

def cut_kmer(seq, num):
	count = 0
	kmer_list = []
	for nt in seq[:(len(seq)-num)]:
		kmer = seq[count:count+num]
		kmer_list.append(kmer)
		count +=1

	return(kmer_list)
# an early version returned a dict.  This now just returns a list.
print(cut_kmer(sequence, number))

