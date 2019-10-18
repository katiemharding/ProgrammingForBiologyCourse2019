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


