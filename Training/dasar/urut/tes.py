#!/usr/bin/env python

def bubble_sort(a):
	n = len(a)
	for i in range(n):
		for j in range(n - i - 1):
			if a[j] > a[j + 1]:
				a[j] += a[j + 1]
				a[j + 1] = a[j] - a[j + 1]
				a[j] -= a[j + 1]
	return a

def taro_sort(a):
	temp_a = []

	while a:
		min = None
		for i in range(len(a)):
			if min:
				if a[i] < min:
					min = a[i]
			else:
				min = a[i]

		temp_a.append(min)
		a.remove(min)

	return temp_a

def selection_sort(a):
	n = len(a)
	masuk = 0
	for i in range(n):
		min_index = i
		for j in range(i + 1, n):
			if a[j] < a[min_index]:
				min_index = j
				masuk = 1

		if masuk:
			a[i] += a[min_index]
			a[min_index] = a[i] - a[min_index]
			a[i] -= a[min_index]
			masuk = 0

	return a

def insertion_sort(a):
	for i in range(len(a)):
		pos = i
		while pos > 0 and a[pos] < a[pos - 1]:
			a[pos] += a[pos - 1]
			a[pos - 1] = a[pos] - a[pos - 1]
			a[pos] -= a[pos - 1]
			pos -= 1
			print a

	return a

def counting_sort(a):
	ember = [0 for i in range(max(a))]
	hasil = []
	
	for i in a:
		ember[i - 1] += 1

	for i in range(len(ember)):
		for j in range(ember[i]):
			hasil.append(i + 1)

	return hasil

a = [5,8,2,3,4,2]

# print bubble_sort(a)
# print taro_sort(a)
# print selection_sort(a)
# print insertion_sort(a)
print counting_sort(a)
