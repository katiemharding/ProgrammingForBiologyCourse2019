dna = "atgcttg"
dna.upper
<built-in method upper of str object at 0x102fa75e0>
dna.upper()
'ATGCTTG'
dna.find('t')
1
dna.count('t')
3
dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'
len.dna
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'dna'
dna.len
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'len'
dna.length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'length'
len(dna)
842
dna.count('A')
167
 bird = 'chicken'
 bird.upper()
'CHICKEN'
 upperBird = bird.upper()
 print(upperBird)
CHICKEN
 mixedDNA = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGtt'
 mixedDNA.upper()
'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTT'
 mixedDNA.replace('T','U')
'GAUGGGAUUggggttttccccUCCCAUGUGCUCAAGACUGGCGCUaaaaGtt'
 mixedDNA.upper.replace('T','U')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'builtin_function_or_method' object has no attribute 'replace'
 mixedDNA.upper().replace('T','U')
'GAUGGGAUUGGGGUUUUCCCCUCCCAUGUGCUCAAGACUGGCGCUAAAAGUU'
 mixedDNA[10:20}
  File "<stdin>", line 1
    mixedDNA[10:20}
                  ^
SyntaxError: invalid syntax
 mixedDNA[10:20]
'gggttttccc'
