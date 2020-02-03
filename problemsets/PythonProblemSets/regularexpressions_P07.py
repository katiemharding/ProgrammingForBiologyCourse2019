#!/usr/bin/env python3

import re
import sys

def find_text(expression, text):
	found = re.findall(expression, text)
	return(found)

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print("please add expression and text to search")
		exit(1)
	expression = sys.argv[1]
	text = sys.argv[2]
	output = find_text(expression, text)
	print("matches found: ", output)
	print("how many found: ", len(output))
