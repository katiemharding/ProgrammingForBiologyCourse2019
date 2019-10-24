#! usr/bin/env

import sys
import datetime

# the user needt to add a file name. make sure they do.
if len(sys.argv) < 2:
	print("please add file name")
	exit(1)

# add dates to log file
now = str(datetime.datetime.now())
now = now[:16] # cut down to date and time

print('# the program and datafile:',' '.join(sys.argv))
print('# was run on ', now)

file_name = sys.argv[1]

needed_info = []
with open(file_name, 'r') as sam_file:
	for line in sam_file:
		line = line.rstrip() # remove whitespace at end
		line_list  = line.split("\t") # split on tab deliminater
		read_name = line_list[0] # first is read name
		gene_info = line_list[2] # third is gene info, need to divide on ^
		gene_name = gene_info.split('^')[0] # this is only gene name, not the transcript
		needed_info.extend([read_name, gene_name])
print(needed_info)

print("done")

