#!/usr/bin/env python

from scripts import HammingDistance

with open('data/hamm.txt') as input_data:
	s, t = [line.rstrip('\n') for line in input_data.readlines()]

count = HammingDistance(s,t)

print count
with open('output/HAMM.txt', 'w') as output_data:
	output_data.write(str(count))
