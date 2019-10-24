#!/usr/bin/env python3

import os, sys

from seqlist_to_kmer import *
# takes one sequence and outputs a list of kmers.  requires 2 inputs seq and number 
from fastq_to_seqlist import *
# seq_from_fastq(file_name) takes a file and outputs a list of sequences
# when you do this it imports and runs that other script.  you have to have the def main(): in that file inorder to run that file.

## method: count_kmers(kmer_list)
##
##  Counts the frequency of each kmer in the given list of kmers
##
##  input parameters:
##
##  kmer_list : list of kmers (type: list)
##               ie.  ["GATC", "TCGA", "GATC", ...]
##                
##
##  returns kmer_counts_dict : dict containing ( kmer : count )
##                    ie.  {  "GATC" : 2,
##                            "TCGA" : 1,
##                             ...       }
    
def count_kmers(kmer_list):
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
	return kmer_count_dict


def main():

	progname = sys.argv[0]
    
	usage = "\n\n\tusage: {} filename.fastq kmer_length num_top_kmers_show\n\n\n".format(progname)
    
	if len(sys.argv) < 4:
		sys.stderr.write(usage)
		sys.exit(1)

    # capture command-line arguments
		fastq_filename = sys.argv[1]
		kmer_length = int(sys.argv[2])
		num_top_kmers_show = int(sys.argv[3])

		seq_list = seq_list_from_fastq_file(fastq_filename)

		all_kmers = list()
    
    #######################
    ## Step 1:
    ## begin your code, populate 'all_kmers' list with the
    ## collection of kmers from all sequences

	for seq in seq_list:
		kmers = seq_to_kmer(seq, kmer_length)
		# all_kmers.append (attaches each as a list (nexted list of kmers for each seq))
		all_kmers.extend(kmers)
		# all kmers and from all sequences in a single list

    ## end your code
    #######################
    
	kmer_count_dict = count_kmers(all_kmers)

	unique_kmers = list(kmer_count_dict.keys())

    #########################
    ## Step 3: sort unique_kmers by abundance descendingly
    ## (Note, you can run and test without first implementing Step 3)
    ## begin your code       hint: see the built-in 'sorted' method documentation

	unique_kmers = sorted(unique_kmers, key = lambda x: kmer_count_dict[x], reverse = True)
    

    ## end your code

    ## printing the num top kmers to show
	top_kmers_show = unique_kmers[0:num_top_kmers_show]
    
	for kmer in top_kmers_show:
 		print("{}: {}".format(kmer, kmer_count_dict[kmer]))
    
        
	ys.exit(0)  # always good practice to indicate worked ok!



#if __name__ == '__main__':
 #   main()
