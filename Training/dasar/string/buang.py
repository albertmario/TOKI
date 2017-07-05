#!/usr/bin/python3

s = input().split()

string = s[0]
hilang = s[1]
hasil = string

while(hilang in hasil):
	hasil = hasil.replace(hilang,'')


print(hasil)