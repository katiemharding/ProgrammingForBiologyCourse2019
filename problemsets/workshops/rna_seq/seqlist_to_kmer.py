#! /usr/bin/env python3

import sys

seq = "AATTGGCC"
num = 2
def cut_kmer(seq, num):
	count = 0
	kmer_list = []
	for nt in seq[:(len(seq)-num)]:
		kmer = seq[count:count+num]
		kmer_list.append(kmer)
		count +=1
	return(kmer_list)

print(cut_kmer(seq, num))


