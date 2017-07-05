#!/usr/bin/python3

a = int(input())

for i in range(a + 1):
	if i % 10 == 0:
		continue
	elif i == 42:
		print("ERROR")
		exit()
	else:
		print(i)

