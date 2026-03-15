#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("Enter the number of elements: ").strip())
    arr = list(map(int, input().rstrip().split()))
    rev=arr[::-1]
    for x in rev:
        print( x,end=" ")