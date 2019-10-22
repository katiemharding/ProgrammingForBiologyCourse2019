#! /usr/bin/env python3

base_file = 'ss_rand5-800_v_qfo'
apend_list = ['_BL50.txt', '_BP62.txt', '_VT10.txt', '_VT160.txt',
'_VT20.txt', '_VT40.txt', '_VT80.txt']

new_list = []
for apend1 in apend_list:
	new_list.append(base_file + apend1)


field_string = "queryid subjectid identity alignmentlength mismatches gapopens qstart qend sstart send evalue bitscore"
# the field string (above) was copied from one output.
fields = field_string.split(' ')
# the above code is now seperted into individual column names
print(fields)
first_row = []

for new in new_list:
	with open(new, 'r') as file1:
		for line in file1:
			if line[0] =='#':
				continue # if the line starts with (first character = 0) skip, continue to next line
			hit_data = dict(zip(fields, line.strip('\n').split('\t')))
			print(hit_data)
	# by striping on \n you remove the language after the \n.  by splitting on '\t' you get each 'column' 
	# the inner dict will be each 'column name'as key with the data as value
			hit_data['file']= new 
			first_row.append(hit_data)
			break # this exits the if loop and leaves only the first row "selected"

for hit in first_row:
	print('\t'.join([hit[x] for x in ('file', 'identity', 'alignmentlength', 'evalue')])) 
	# this prints just these subdictionaries in that order
