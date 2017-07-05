#!/usr/bin/python3

import math

a = int(input())
first = 0
b = a

for i in range(2, int(math.sqrt(a)) + 1):
	count = 0

	while a % i == 0:
		count += 1
		a //= i

	if count > 1:
		if first == 0:
			print("%d^%d" % (i, count), end="")
		else:
		 	print(" x %d^%d" % (i, count), end="")
		first = 1
	elif count == 1:
		 if first ==0:
		 	print("%d" % i, end="")
		 else:
		 	print(" x %d" % i, end="")
		 first = 1

if a > 1:
	if b == a:
		print("%d" % b)
	else:
		print(" x %d" % a)
else:
	print()