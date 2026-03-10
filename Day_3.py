#!/bin/python3
import math
import os
import random
import re
import sys

def check(N):

    if N%2==1:
        print("Weird")
    if N%2==0 and 2<=N<=5:
        print("Not Weird")
    if N%2==0 and 6<=N<=20:
        print("Weird")
    if N%2==0 and N>20:
        print("Not Weird")

if __name__ == '__main__':
    N = int(input("Enter a positive integer: ").strip())
    check(N)
