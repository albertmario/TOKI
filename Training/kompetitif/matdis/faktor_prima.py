#!/usr/bin/env python

import math

n = int(input())
hasil = ""

def isPrime(n):
	temp = int(math.sqrt(n) + 1)
	for i in range(2, temp):
		if n % i == 0:
			return 0
	return 1

temp = int(math.sqrt(n) + 2)

for i in range(2, temp):
	count = 0
	if isPrime(i):
		while(n % i == 0):
			count += 1
			n /= i

		if count > 1:
			if hasil == "":
				hasil += ("%d^%d" % (i, count))
			else:

				hasil += (" x %d^%d" % (i, count))
		elif count:
			if hasil == "":
				hasil += ("%d" % i)
			else:
				hasil += (" x %d" % i)

if n > 1:
	if hasil == "":
		hasil += ("%d" % n)
	else:
		hasil += (" x %d" % n)

print(hasil)