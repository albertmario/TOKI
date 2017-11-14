#!/usr/bin/env python

def sort(h, W):
	n = len(h)
	masuk = 0
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if h[j] > h[min_index]:
				min_index = j
				masuk = 1
		if masuk:
			# print(min_index)
			temp = h[min_index]
			h[min_index] = h[i]
			h[i] = temp

			temp = W[min_index]
			W[min_index] = W[i]
			W[i] = temp

			masuk = 0

	return h, W

masuk = input().split()
N = masuk[0]
X = int(masuk[1])

W = input().split()
W = [int(i) for i in W]

C = input().split()

h = [int(C[i])*1.0 / int(W[i]) for i in range(len(W))]
h, W = sort(h, W)
hasil = 0.0
a = 0

for i in range(X):
	try:
		hasil += h[a]
	except:
		break
	W[a] -= 1
	if W[a] == 0:
		a += 1

print("%.5f" % hasil)