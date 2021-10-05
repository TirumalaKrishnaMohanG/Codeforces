#!/usr/bin/env python

# Headers
import os

# Input
get_IN = int(input())
c = 0

# Filter the Count
for i in range(get_IN):
	get_STR = input()
	if get_STR == 'Icosahedron':
		c += 20

	if get_STR == 'Cube':
		c += 6

	if get_STR == 'Tetrahedron':
		c += 4

	if get_STR == 'Octahedron':
		c += 8

	if get_STR == 'Dodecahedron':
		c += 12

print(c)