#!/usr/bin/env python

# Headers
import os

# Input
in_val = input().replace(',','').replace('{','').replace('}','').replace(' ','')

# Count to calculate{}
print(len(set(sorted(list(in_val)))))