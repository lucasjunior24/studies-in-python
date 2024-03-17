#!/bin/python3

import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    letf_right = right_left = 0
    laps = 0
    for i in range(len(arr)):
        line = arr[i]
        
        letf_right += line[laps]
        right_left += line[len(line) - laps - 1]
        laps += 1

    # for i in range(len(arr)):
    #     letf_right += arr[i][i]
    #     right_left += arr[i][len(arr)-1-i]


    print(letf_right, right_left, abs(letf_right - right_left))
    return abs(letf_right - right_left)

if __name__ == '__main__':

    # n = int(input().strip())

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)