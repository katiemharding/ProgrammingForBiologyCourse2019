#!/usr/bin/env python3

import re
import sys

def find_line(expression, replacement, text):
	line_list = [] # create empty list to store line marker
	line_count = 0
	new_file_name = replacement + "_" + text # give the new file a name
	new_file = open(new_file_name , "w") # this will save the new file with changes
	with open(text, "r") as new_text:
		for rawline in new_text:
			line = rawline.rstrip()
			found = re.findall(expression, line)
			if len(found) >0:
				line_list.append(line_count)
				new_file.write((line.replace(expression, replacement) + "\n")) 
				# add the line. add return to put next on new line  
				line_count += 1 # each line gets a count
			else:
				line_count += 1 # each line gets a count
				new_file.write((line + "\n"))
	new_file.close() # the with open statement closes the file.  the open(file) needs to be closed
	print("Wrote to file: ", str(new_file_name)) # it's nice to tell the user you wrote a file
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
