#!/usr/bin/env python

import math

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

def solve(kode, m, M, n, N):
	global arr
	a,b,c,d = m, M, n, N
	for i in kode:
		m, M, n, N = a,b,c,d
		temp = i[1:]
		for j in temp:
			bantu_baris = (M + m) // 2
			bantu_kolom = (N + n) // 2

			if j == '0': 
				M = bantu_baris
				N = bantu_kolom
			elif j == '1': 
				M = bantu_baris
				n = bantu_kolom
			elif j == '2': 
				m = bantu_baris
				N = bantu_kolom
			elif j == '3': 
				m = bantu_baris
				n = bantu_kolom

		for j in range(m, M):
			for k in range(n, N):
				arr[j][k] = '1'

count = int(input())
kode = []
arr = []

for i in range(count):
	kode.append(input())

MN = input().split()
M = int(MN[0])
N = int(MN[1])

M_baru, N_baru = extend(M,N)
arr = [['0' for j in range(N_baru)] for i in range(M_baru)]
solve(kode, 0, M_baru, 0, N_baru)

for i in range(M):
	for j in range(N):
		if j == N - 1:
			print(arr[i][j], end = "")
		else:
			print(arr[i][j], end = " ")
	print(end = "\n")