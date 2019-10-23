#! /usr/bin/env python3

import subprocess

base_url200ss = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo'
base_url800ss = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-800_v_qfo'
base_url200blas = 'https://fasta.bioch.virginia.edu/mol_evol/data/blast_rand5-200_v_qfo'
base_url = 'https://fasta.bioch.virginia.edu/mol_evol/data/blast_rand5-800_v_qfo'
example_url = 'https://fasta.bioch.virginia.edu/mol_evol/data/ss_rand5-200_v_qfo_BP62.txt'

file_listss = ['_BL50.txt', '_BP62.txt', '_VT10.txt', '_VT160.txt', '_VT20.txt', '_VT40.txt', '_VT80.txt']
file_list = ['_BLOSUM62.txt', '_BLOSUM80.txt', '_PAM30.txt', '_PAM70.txt'] 
for file1 in file_list:
	file_new = (base_url + file1)
	print(file_new)
	subprocess.run(['wget', file_new])

print('done')
