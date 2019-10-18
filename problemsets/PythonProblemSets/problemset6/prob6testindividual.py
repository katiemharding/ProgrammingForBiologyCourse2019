#! /usr/bin/env python3

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

