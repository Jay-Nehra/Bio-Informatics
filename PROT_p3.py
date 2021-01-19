#!/usr/bin/env python

from scripts import ProteinDictRNA

with open('data/prot.txt') as input_data:
	s = input_data.read().rstrip('\n')

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()

s_protein = ''
for i in range(0,len(s),3):
    if rna_dict[s[i:i+3]] != 'Stop':
        s_protein+= rna_dict[s[i:i+3]]

print s_protein

with open('output/PROT.txt', 'w') as output_data:
	output_data.write(s_protein)
