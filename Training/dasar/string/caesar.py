#!/usr/bin/pyhton3

s = input()
K = int(input())
hasil = ''

for i in s:
	temp = K + ord(i)
	if temp > 122:
		temp = (temp - 122) + 96

	hasil += chr(temp)

print(hasil)