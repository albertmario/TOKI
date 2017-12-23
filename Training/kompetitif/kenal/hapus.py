#!/usr/bin/env python

a = input()
b = input()
temp = ""
# print()
for i in range(len(a)):
	temp = a[0:i] + a[i+1:]
	if temp == b:
		print("Tentu saja bisa!")
		exit()
print("Wah, tidak bisa :(")
