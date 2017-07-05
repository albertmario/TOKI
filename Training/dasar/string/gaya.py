#!/usr/bin/python3

import string

def camel(s):
	s = s.split('_')
	hasil = s[0]
	for i in s[1:]:
		temp = i[0].upper() + i[1:]
		hasil += temp

	return hasil

def snake(s):
	hasil = ''
	for i in s:
		if i in string.ascii_uppercase:
			hasil += '_'+i.lower()
		else:
			hasil += i
	return hasil

s = input()

if '_' in s:
	print(camel(s))
else:
	for i in s:
		if i in string.ascii_uppercase:
			print(snake(s))
			exit()
	print(s)