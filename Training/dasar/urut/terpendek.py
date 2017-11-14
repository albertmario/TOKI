#!/usr/bin/env python

masuk = input().split()
N = masuk[0]
K = int(masuk[1])

tinggis = input().split()
tinggi = [int(i) for i in tinggis]
n = len(tinggi)

for i in range(n):
	for j in range(n - i - 1):
		if tinggi[j] > tinggi[j + 1]:
			tinggi[j] += tinggi[j + 1]
			tinggi[j + 1] = tinggi[j] - tinggi[j + 1]
			tinggi[j] -= tinggi[j + 1]

print(tinggi[K - 1])
