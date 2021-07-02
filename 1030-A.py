#!/usr/bin/env python

# Headers files
import sys

# Input
get_COUNT = input()
get_LIST = input()

# Function to find the problem status
def find_problem():
	get_RES = ''.join(['HARD' if "1" in str(get_LIST) else "EASY"])
	return get_RES

if __name__ == '__main__':
	print(find_problem())