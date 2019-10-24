#! /usr/bin/env python3

import sys

file_name = sys.argv[1]
# this is the solution presented in class:
def seq_from_fastq(file_name):

	sequences  = [] #create empty list
	fh = open(file_name) # open file
	counter = 0 # start counter
	for line in fh: # for line in file
		line = line.rstrip() # remove white space
		counter += 1 # add one to counter to get running tally of the number of lines
		if (counter %4 == 2): # the sequence is always line 2.  
		# %4 means return the remainder of count/4
		# this means it will return the second of each record
			sequences.append(line)
	return(sequences)

print(seq_from_fastq(file_name))
# note that the program returns a list




