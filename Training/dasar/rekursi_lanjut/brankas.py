#!/usr/bin/env python

from itertools import permutations
import string
tampung = []

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

def cek(p):
	global tampung

	if tuple(sorted(p)) in tampung:
		return False
	else:
		tampung.append(tuple(sorted(p)))
		return True

NK = input().split()
N = int(NK[0])
K = int(NK[1])

for p in unique_permutations(string.digits[1:N + 1], K):
	if cek(p):
		print(" ".join(p))