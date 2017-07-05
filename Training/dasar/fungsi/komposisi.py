#!/usr/bin/python3

bil = input().split()
A = int(bil[0])
B = int(bil[1])
K = int(bil[2])
x = int(bil[3])

fx = abs(A*x + B)

for i in range(K - 1):
	x = fx
	fx = abs(A*x + B)

print(fx)