#! /usr/bin/env python3

import subprocess

output_file = "GCoutputfile.txt"
with open(output_file, "w") as ofh:
	oops = subprocess.check_call('python3' 'calculate_GC_content.py' 'dna1.txt', stdout = ofh)
print(oops)
#outputfile2 = "dnacut.txt"
#with open(outputfile2, "w") as ofh:
#	if oops == 0:
#		oops2 = subprocess.check_call('python3' 'dna_cutting.py' 'dna1.txt', stdout = ofh)

