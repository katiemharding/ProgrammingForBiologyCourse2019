#!/usr/bin/env python3
import sys
# for testing assign a number to a value
unknown_number = int(sys.argv[1])
# first test if it is positive
if unknown_number>0:
	print(unknown_number, "is positive")
	if unknown_number > 50:
		print(unknown_number, "is bigger than 50")
	else:
		print(unknown_number, "is less than 50")
		if unknown_number%2 == 0:
			print(unknown_number, "is even")
		else:
			print(unknown_number, "is odd")
# What to do if not positive:
# test if equals 0
elif unknown_number == 0:
	print("equals 0")
# if not positive test if negative?
else:
	print(unknown_number, "is negative")

