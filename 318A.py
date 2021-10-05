#!/usr/bin/env python

n,k = input().split()
n,k =int(n),(int(k)-1)
get_RES = [x for x in range(1,int(n)+1) if x%2!=0]+[x for x in range(1,int(n)+1) if x%2==0]
print(get_RES[k])
