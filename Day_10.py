#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    k=bin(n)
    k=k.replace("0b", "")
   
    count=0
    max=0
    for i in k:
        if i=='1':
            count=count +1
           
        else:
            count=0
        if count>max:
            max=count     
    print(max)