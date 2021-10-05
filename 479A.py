#!/usr/bin/env python

# Headers
import os

# Input
a = int(input())
b = int(input())
c = int(input())

# Calx
aa = a+b*c
bb = a*(b+c)
cc = a*b*c
dd = (a+b)*c
ee = a*b+c
ff = a+b+c

fin = max(aa,bb,cc,dd,ee,ff)
print(fin)
