#!/usr/bin/env python3

import re
import sys

def find_line(expression, replacement, text):
	line_list = [] # create empty list to store line marker
	line_count = 0
	new_text = replacement + text # give the new file a name
	new_file = open(new_text , "w")
	with open(text, "r") as new_text:
		for rawline in new_text:
			line = rawline.rstrip()
			found = re.findall(expression, line)
			if len(found) >0:
				line_list.append(line_count)
				new_file.write(line.replace(expression, replacement)) # add the line.  
				line_count += 1 # each line gets a count
			else:
				line_count += 1 # each line gets a count
				new_file.write(line)
	new_file.close()
	print("Wrote to file:", new_file) # it's nice to tell the user you wrote a file
	return(line_list) # Line list is the location of each text.  

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print("please add expression and text to search")
		exit(1)
	expression = sys.argv[1]
	replacement = sys.argv[2]
	text = sys.argv[3]
	output = find_line(expression, replacement, text)
	print("matches found: ", output)
	print("how many found: ", len(output))
