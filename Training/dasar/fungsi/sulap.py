#!/usr/bin/python3

int(input())
kamus = {}
kamus['A'] = input().split()
kamus['B'] = input().split()

# print(kamus)
Q = int(input())
for i in range(Q):
	temp = input().split()
	cmd1 = temp[0]
	index1 = int(temp[1])
	cmd2 = temp[2]
	index2 = int(temp[3])

	tmp2 = kamus[cmd1][index1 - 1]
	kamus[cmd1][index1 - 1] = kamus[cmd2][index2 - 1]
	kamus[cmd2][index2 - 1] = tmp2



for i in sorted(kamus):
	for j in range(len(kamus[i])):
		if j == len(kamus[i]) - 1:
			print(kamus[i][j], end="\n")
		else:
			print(kamus[i][j], end=" ")