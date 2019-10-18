#! /usr/bin/env python3

# Problem 1)
# on the command line type:
# wget https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_06.txt
# this downloads and saves the file to your workspace
# first open the file to python

with open('Python_06.txt', 'r') as file_object:
	for rawline in file_object:
		line = rawline.rstrip()
		Upper_line = line.upper()
		print(Upper_line)

