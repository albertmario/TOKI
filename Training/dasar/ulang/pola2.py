#!/usr/bin/python3

a = int(input())

for i in range(1, a+1):
	temp = " "*(a-i) + '*'*i
	print(temp, end="\n")