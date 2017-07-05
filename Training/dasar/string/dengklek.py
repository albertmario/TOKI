#!/usr/bin/pyhton3

a = input()
hasil = ''

for i in a:
	if i.islower():
		hasil += i.upper()
	else:
		hasil += i.lower()

print(hasil)