#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    mul=1
    for x in range(1,n+1):
        mul=mul*x
    return mul
if __name__ == '__main__':
    n = int(input("Enter a number: ").strip())

    result = factorial(n)
    print(result)