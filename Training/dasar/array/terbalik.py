#!usr/bin/python3

import sys

hasil = []

for line in sys.stdin:
	hasil.append(line.split('\n')[0])

for i in hasil[::-1]:
	print(i)