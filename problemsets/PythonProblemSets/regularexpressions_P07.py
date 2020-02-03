#!/usr/bin/env python3

import re
import sys

def find_line(expression, text):
	line_list = [] # create empty list to store line marker
	line_count = 0
	with open(text, "r") as new_text:
		for rawline in new_text:
			line = rawline.rstrip()
			found = re.findall(expression, line)
			if len(found) >0:
				line_list.append(line_count)
				line_count += 1 # each line gets a count
			else:
				line_count += 1 # each line gets a count
	return(line_list)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("please add expression and text to search")
		exit(1)
	expression = sys.argv[1]
	text = sys.argv[2]
	output = find_line(expression, text)
	print("matches found: ", output)
	print("how many found: ", len(output))
