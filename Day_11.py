#!/bin/python3

import sys

def hourglassSum(arr):
    max_sum = float('-inf')  # handle negative values
    
    for i in range(4):  # rows (0 to 3)
        for j in range(4):  # columns (0 to 3)
            
            current_sum = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            
            max_sum = max(max_sum, current_sum)
    
    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(result)