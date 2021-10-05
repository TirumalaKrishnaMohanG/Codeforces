#!/usr/bin/env python
a = int(input())
b = [int(x) for x in input().split()]
b.sort()
for x in (b):
	print(x,end=" ")