#!/usr/bin/python3

import math

a = int(input())
hasil = []

for i in range(1, int(math.sqrt(a)+1)):
	if a % i == 0 :
		if a / i == i:
			hasil.append(a//i)
		else:
			hasil.append(a//i)
			hasil.append(i)

for i in list(sorted(hasil))[::-1]:
	print(i)