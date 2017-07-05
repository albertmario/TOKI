#!/usr/bin/python3

ND = input().split()
N = int(ND[0])
D = int(ND[1])

temp = []

for i in range(N):
	XY = input().split()
	temp.append(XY)

min = None
max = None

for i in range(len(temp) - 1):
	for j in range(i+1, len(temp)):
		if min == None and max == None:
			min = pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D)
			max = pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D)
		else:
			if pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D) > max:
				max = pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D)

			if pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D) < min:
				min = pow(abs(int(temp[i][0]) - int(temp[j][0])), D) + pow(abs(int(temp[i][1]) - int(temp[j][1])), D)

print("%d %d" % (min, max))
