
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("Enter a number: ").strip())
    print(f"Multiplication table of {n}:")
    for x in range(1,11):
        print(f"{n} x {x} =",n*x)
