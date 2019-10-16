#!/usr/bin/env python3
import sys
unknown_number = int(sys.argv[1])
if unknown_number>0:
	print(unknown_number, "is positive")
elif unknown_number == 0:
	print("equals 0")
else:
	print(unknown_number, "is negative")

