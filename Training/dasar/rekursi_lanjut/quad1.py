#!/usr/bin/env python

import math

count = 0
hasil = []
arr = []

def extend(M,N):
	if M > N:
		while math.log(M,2) != int(math.log(M,2)):
			M += 1
		N = M
	else:
		while math.log(N,2) != int(math.log(N,2)):
			N += 1
		M = N

	return M, N

def solve(arr, m, M, n, N, kode):
	temp = None
	bagi = 0

	for i in range(m, M):
		for j in range(n, N):
			if temp == None:
				temp = arr[i][j]
				continue

			if arr[i][j] != temp:
				bagi = 1
	if bagi:
		bantu_baris = (m + M) // 2
		bantu_kolom = (n + N) // 2

		solve(arr, m, bantu_baris, n, bantu_kolom, kode + '0')
		solve(arr, m, bantu_baris, bantu_kolom, N, kode + '1')
		solve(arr, bantu_baris, M, n, bantu_kolom, kode + '2')
		solve(arr, bantu_baris, M, bantu_kolom, N, kode + '3')
		return

	if temp == '1':
		global count, hasil
		count += 1
		hasil.append('1' + kode)

	return


MN = input().split()
M = int(MN[0])
N = int(MN[1])

for i in range(M):
	arr.append(input().split())

M_baru, N_baru = extend(M,N)

for i in range(M_baru - M):
	arr.append(['0' for j in range(len(arr[0]))])

for i in arr:
	for j in range(N_baru - N):
		i.append('0')

solve(arr, 0, M_baru, 0, N_baru, '')

print(count)
for i in hasil:
	print(i)