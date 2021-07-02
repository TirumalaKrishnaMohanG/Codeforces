#!/usr/bin/env python

# Header files
import sys

# Input
get_IN = input()

# Fn to find the instructions
def find_instruction():
	get_STR = ''.join(["YES" if 'H' in get_IN or 'Q' in get_IN or '9' in get_IN else "NO"])
	return get_STR

# Calling the main
if __name__ =='__main__':
	print(find_instruction())
