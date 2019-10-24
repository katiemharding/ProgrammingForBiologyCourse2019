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

	kmer_dict = {} #empty dict
	for kmer in kmer_list: 
	# is this kmer in our dictionary?
		if kmer in kmer_dict:
    # if it is, lets increment our count
			previous_count = kmer_dict[kmer]
			new_count = previous_count + 1
			kmer_dict[kmer] = new_count
		else:
    # if not, lets add this nt to our dictionary and make count = 1
			kmer_dict[kmer] = 1;

	return(kmer_dict)

print(cut_kmer(sequence, number))

