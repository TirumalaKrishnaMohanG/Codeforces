#!/usr/bin/env python

# Input
n = int(input())
# Count for rooms
c = 0
for i in range(1,n+1):
	p,q = input().split()
	p,q = int(p),int(q)
	if p == q:
		c +=0
	elif p >= q or p <= q:
		c +=1
print(c)	
