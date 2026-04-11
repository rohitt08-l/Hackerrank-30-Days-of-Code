#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    nswap=0
    for i in a:
        for j in range (len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                nswap=nswap+1
        if nswap==0:
            break
print(f"Array is sorted in {nswap} swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
