#!/usr/bin/env python

# Headers
import os

# Input
n,k = input().split()
n,k = int(n),int(k)

for i in range(1,k+1):
	temp = n%10
	if temp ==  0:
		n = n/10;
	else:
		n = n-1;

print(int(n))