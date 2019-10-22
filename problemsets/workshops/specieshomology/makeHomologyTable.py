#! /usr/bin/env python3

import subprocess

base_url200 = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo'
base_url = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-800_v_qfo'
example_url = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_BP62.txt'

file_list = ['_BL50.txt', '_BP62.txt', '_VT10.txt', '_VT160.txt', '_VT20.txt', '_VT40.txt', '_VT80.txt']

for file1 in file_list:
	file_new = (base_url + file1)
	print(file_new)
	subprocess.run(['wget', file_new])

print(done)
