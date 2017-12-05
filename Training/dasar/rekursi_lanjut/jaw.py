#!/usr/bin/env python

count = 0
arr = []

def solve(B, K, warna):
	global arr
	global count
	global M, N
	m, n = M - 1, N - 1

	arr[B][K] = '*'
	count += 1

	if B - 1 <= m and K <= n and B - 1 >= 0 and K >= 0:
		if arr[B - 1][K] == warna:
			solve(B - 1, K, warna)
	if B + 1 <= m and K <= n and B + 1 >= 0 and K >= 0:
		if arr[B + 1][K] == warna:
			solve(B + 1, K, warna)
	if B <= m and K + 1 <= n and B >= 0 and K + 1>= 0:
		if arr[B][K + 1] == warna:
			solve(B, K + 1, warna)
	if B <= m and K - 1 <= n and B >= 0 and K - 1 >= 0:
		if arr[B][K - 1] == warna:
			solve(B, K - 1, warna)

	return

MN = input().split()
M = int(MN[0])
N = int(MN[1])

for i in range(M):
	arr.append(input().split())

BK = input().split()
B = int(BK[0])
K = int(BK[1])
warna = arr[B][K]
# print(warna)
solve(B, K, warna)

# for i in arr:
	# print(i)

print(count * (count - 1))