#!/usr/bin/env python
# Headers
import sys

# Input
get_COUNT = input()
get_IN = input()

# Fn to count strings
def count_strings():
	get_STR = [x for x in get_IN]
	str1,str2=get_STR.count('A'),get_STR.count('D')
	if str1 > str2:
		result = ("Anton")
	elif str2 > str1:
		result =("Danik")
	else:
		result = ("Friendship")
	return result

if __name__ == "__main__":
	print(count_strings())
