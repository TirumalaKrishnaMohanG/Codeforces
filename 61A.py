#!/usr/bin/env python

# Headers
import os

# Input
a = (input())
b = (input())

fin_RES = bin(int(a,2)+int(b,2))
print(fin_RES.replace('0b',''))