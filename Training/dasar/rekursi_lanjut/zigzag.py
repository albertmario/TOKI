#!/usr/bin/env python

from itertools import permutations
import string


def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

def cek(nilai):
	x = 0
	benar = 0
	while 1:
		try:
			temp = nilai[x:x+3]
			if (temp[1] < temp[0] and temp[1] < temp[2]) or (temp[1] > temp[0] and temp[1] > temp[2]):
				benar = 1
			else:
				return False
			x += 1
		except:
			break

	if benar:
		return True

n = int(input())
for p in unique_permutations(string.digits[1:n+1], n):
    temp = ("".join(p))
    if n > 2:
    	if cek(temp):
    		print(temp)
    else:
    	print(temp)