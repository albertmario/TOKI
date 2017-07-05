#!/usr/bin/python3

def cari(berat, x, y):
	kiri = 0
	kanan = len(berat) - 1

	while (kanan - kiri) != 1:
		tengah = (kanan - kiri) // 2
		if x > int(berat[tengah]):
			kiri = tengah
		else:
			kanan = tengah

	if int(berat[kiri]) > x:
		hasilkiri = int(berat[kiri])
	else:
		hasilkiri = int(berat[kanan])

	print(hasilkiri)


N = int(input())
berat = input().split()
tanya = int(input())

for i in range(tanya):
	berat_temp = []
	berat_temp.extend(berat)

	batas = input().split()
	x = int(batas[0])
	y = int(batas[1])
	cari(berat, x, y)
