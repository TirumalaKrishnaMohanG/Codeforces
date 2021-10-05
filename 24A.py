#!/usr/bin/env python

# Heders
import os

# Input
n = int(input())
k = [int(x) for x in input().split()]
e,o =[],[]
even,odd = 0,0
# Finding the odd one in list
for i in k:
	if i%2 == 0:
		e.append(str(k.index(i)))
	elif i%2 == 1:
		o.append(str(k.index(i)))


if len(o) <= 1:
	val = int(''.join(o))+1
	print(val)
elif len(e) <= 1:
	val = int(''.join(e))+1
	print(val)


	