#!/usr/bin/env python

import os, sys



## method: seq_list_from_fastq_file(fastq_filename)
##
##  Extracts the sequence lines from a fastq file and returns a list
##  of the sequence lines
##
##  input parameters:
##
##  fastq_filename :  name of the fastq file (type: string)
##
##  returns seq_list : list of read sequences.
##                    ie.  ["GATCGCATAG", "CGATGCAG", ...]
    
def seq_list_from_fastq_file(fastq_filename):

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

def main():

    progname = sys.argv[0]
    
    usage = "\n\n\tusage: {} filename.fastq num_seqs_show\n\n\n".format(progname)
    
    if len(sys.argv) < 3:
        sys.stderr.write(usage)
        sys.exit(1)

    # capture command-line arguments
    fastq_filename = sys.argv[1]
    num_seqs_show = int(sys.argv[2])

    seq_list = seq_list_from_fastq_file(fastq_filename)

    print(seq_list[0:num_seqs_show])

    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()
# any script can be a drver script   
