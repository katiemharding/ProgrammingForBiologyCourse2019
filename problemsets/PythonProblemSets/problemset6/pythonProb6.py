#! /usr/bin/env python3

# Problem 1)
# on the command line type:
# wget https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.txt
# this downloads and saves the file to your workspace
# first open the file to python

# problem 2) write the file to another file
with open('Python_06.txt', 'r') as file_object, open('Python_06_uc.txt', 'w') as song_write:
	for rawline in file_object:
		line = rawline.rstrip()
		Upper_line = line.upper()
		print(Upper_line)
	#if you indent to here is only prints the last line to file	
		# song_write.write(Upper_line) this code prints as one long string with white space
		#you have to indent twice to get the whole file printed
		song_write.write(Upper_line +'\n')
print("wrote Python_06_uc.txt")


# prob 3 open and print reverse seq 
# command line: wget https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.seq.txt
genes={}

with open('Python_06.seq.txt', 'r') as unk_seq:
	for rawline in unk_seq:
		line = rawline.rstrip() # remove white space at end
		gene_id, seq = line.split() # split on white space in the middle
		genes[gene_id] = seq # assign to dictionary
	print(genes)
# on the command line type
# python3 prob6testindividual.py > Python06_seq_dict.txt

# number 4 for this they just want total lines, average line, total characters
total_nt = 0
line_count = 0

with open('Python_06.fastq', 'r') as unk_file:
	for rawline in unk_file:
		line = rawline.rstrip()
		# each gene has 4 things
	    # @ indicates ID
		# no start indicates seq
        # + indicates sequence ID (gene_id) from before
        # quality
		line_count += 1 # add one per line
		nt_count = len(line) # find length of line
		total_nt +=nt_count # add lengths to get each line
	print("line count is:", line_count)
	print("total count is:", total_nt)
 	ave_nt_line = total_nt/line_count # average is totoal nt/line
	print("average nt per line:", ave_nt_line)

