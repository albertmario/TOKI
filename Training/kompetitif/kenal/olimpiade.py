#!/usr/bin/env python

T = int(input())

def sort3():
	n = len(nama)
	for i in range(n):
		for j in range(n - i - 1):
			if skor3[j] > skor3[j + 1]:
				temp = nama[j]
				nama[j] = nama[j + 1]
				nama[j + 1] = temp

				skor3[j] += skor3[j + 1]
				skor3[j + 1] = skor3[j] - skor3[j + 1]
				skor3[j] -= skor3[j + 1]

				skor2[j] += skor2[j + 1]
				skor2[j + 1] = skor2[j] - skor2[j + 1]
				skor2[j] -= skor2[j + 1]

				skor1[j] += skor1[j + 1]
				skor1[j + 1] = skor1[j] - skor1[j + 1]
				skor1[j] -= skor1[j + 1]

def sort2():
	n = len(nama)
	for i in range(n):
		for j in range(n - i - 1):
			if skor3[j] == skor3[j + 1]:
				if skor2[j] > skor2[j + 1]:
					temp = nama[j]
					nama[j] = nama[j + 1]
					nama[j + 1] = temp

					skor2[j] += skor2[j + 1]
					skor2[j + 1] = skor2[j] - skor2[j + 1]
					skor2[j] -= skor2[j + 1]

					skor1[j] += skor1[j + 1]
					skor1[j + 1] = skor1[j] - skor1[j + 1]
					skor1[j] -= skor1[j + 1]

def sort1():
	n = len(nama)
	for i in range(n):
		for j in range(n - i - 1):
			if skor3[j] == skor3[j + 1]:
				if skor2[j] == skor2[j + 1]:
					if skor1[j] > skor1[j + 1]:
						temp = nama[j]
						nama[j] = nama[j + 1]
						nama[j + 1] = temp

						skor1[j] += skor1[j + 1]
						skor1[j + 1] = skor1[j] - skor1[j + 1]
						skor1[j] -= skor1[j + 1]

def cek(nama, M, target):
	temp = nama[::-1]
	for i in range(M):
		if temp[i] == target:
			return 1
	return 0


for i in range(T):
	NM = input().split()
	N = int(NM[0])
	M = int(NM[1])

	target = input()
	nama = []
	skor1 = []
	skor2 = []
	skor3 = []

	for j in range(N):
		datas = input().split()
		nama.append(datas[0])
		skor1.append(int(datas[1]))
		skor2.append(int(datas[2]))
		skor3.append(int(datas[3]))

	sort3()
	sort2()
	sort1()

	if cek(nama, M, target):
		print("YA")
	else:
		print("TIDAK")