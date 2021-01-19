#!/usr/bin/env python
import os
import random


# biopython
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from sys import *

from scripts import ReadFASTA, ProteinDictDNA

dna_list = ReadFASTA('data/splc.txt')
exon = dna_list[0][1]

# Remove the introns.
for intron in dna_list[1:]:
	exon = exon.replace(intron[1], '')

# Translate the exons.
dna_dict = ProteinDictDNA()
exon_protein = ''
for index in range(0, len(exon), 3):
	exon_protein += dna_dict[exon[index:index+3]] if dna_dict[exon[index:index+3]]  != 'Stop' else ''

print (exon_protein)
with open('output/SPLC.txt', 'w') as output_data:
	output_data.write(exon_protein)
