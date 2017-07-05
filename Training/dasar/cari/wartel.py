#!/usr/bin/python3

NQ = input().split()
N = int(NQ[0])
Q = int(NQ[1])

buku = {}
for i in range(N):
	temp = input().split()
	buku[temp[0]] = temp[1]

for i in range(Q):
	temp = input()
	if temp in buku:
		print(buku[temp])
	else:
		print("NIHIL")