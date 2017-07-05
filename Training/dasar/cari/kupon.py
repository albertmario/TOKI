#!/usr/bin/python3

NX = input().split()
X = int(NX[1])
kupon = input().split()
min = None

for i in kupon:
	if min == None:
		min = abs(int(i) - X)
		hasil = i
	else:
		if abs(int(i) - X) < min:
			min = abs(int(i) - X)
			hasil = i
		elif abs(int(i) - X) == min:
			if i < hasil:
				hasil = i

print(hasil)