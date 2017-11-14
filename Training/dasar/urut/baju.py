#!/usr/bin/env python

def sort(nilai):
	m = max(nilai)
	n = len(nilai)

	ember = [0 for i in range(m)]
	hasil = []

	for i in nilai:
		ember[i - 1] += 1

	for i in range(len(ember)):
		for j in range(ember[i]):
			hasil.append(i + 1)
	
	return hasil

N = int(input())
nilai = []

for i in range(N):
	nilai.append(int(input()))

nilai = sort(nilai)
if len(nilai) % 2:
	print("%.1f" % (nilai[len(nilai) // 2] * 1.0))
else:
	print("%.1f" % ((nilai[len(nilai) // 2] + nilai[len(nilai) // 2 - 1]) * 1.0 / 2))