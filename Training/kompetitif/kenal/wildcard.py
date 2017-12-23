#!/usr/bin/env python

patt = input()
n = int(input())
hasil = []

def ujung(depan = 0):
	global patt
	global n
	global hasil

	if depan:
		patt = patt[::-1]
	for i in range(n):
		if depan:
			a = input()[::-1]
		else:
			a = input()
		for j in range(len(patt)):
			if patt[j] == '*':
				if depan:
					print(a[::-1])
				else:
					print(a)
			else:
				if patt[j] != a[j]:
					break
	pass

def tengah():
	global patt
	global n
	global hasil


	for i in range(n):
		benar = 0
		a = input()
		for j in range(len(patt)):
			if patt[j] == '*':
				benar += 1
				break
			else:
				if patt[j] != a[j]:
					break

		patt = patt[::-1]
		a = a[::-1]
		for j in range(len(patt)):
			if patt[j] == '*':
				benar += 1
				if benar == 2:
					print(a[::-1])
			else:
				if patt[j] != a[j]:
					break

		patt = patt[::-1]
	pass

def all():
	global patt
	global n
	global hasil

	for i in range(n):
		a = input()
		print(a)
	pass

if patt[0] == '*':
	if patt[-1] == '*':
		continue
	else:
		ujung(depan = 1)
else:
	if patt[-1] == '*':
		ujung()
	else:
		tengah()
	
# for j in hasil:
	# print(j)