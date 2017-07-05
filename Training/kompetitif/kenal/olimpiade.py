#!/usr/bin/python3

T = int(input())

for i in range(T):
	NM = input().split()
	N = int(NM[0])
	M = int(NM[1])
	targetID = input()
	for j in range(N):
		data = input().split()
