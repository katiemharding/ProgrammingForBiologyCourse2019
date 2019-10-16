#!/usr/bin/env python3
import sys
# for testing assign a number to a value
unknown_number = int(sys.argv[1])
# first test if it is positive
if unknown_number>0:
	print(unknown_number, "is positive")
	if unknown_number > 50:
# modulo (%) returns the remainder.  allows testing if divisible by
		if unknown_number%3 == 0:
			print(unknown_number, "is larger than 50 and divisible by 3")
		else:
			print(unknown_number, "is bigger than 50")
	elif unknown_number == 50:
			print(unknown_number, "is even and equal to 50")
	else:
		print(unknown_number, "is less than 50")
# modulo tests if a number is even.
# it returns the remainder (the numbers remaining after division)
# if it is zero then there is no remainder
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

