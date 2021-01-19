#!/usr/bin/env python

with open('data/rna.txt') as input_data:
	dna = input_data.read().strip()

with open('output/RNA.txt', 'w') as output_data:
	output_data.write(dna.replace('T', 'U'))
	print (dna.replace('T', 'U'))
