#!/usr/bin/python3

angka = input().split()
a = int(str(int(angka[0]))[::-1])
b = int(str(int(angka[1]))[::-1])
print(int(str(a+b)[::-1]))