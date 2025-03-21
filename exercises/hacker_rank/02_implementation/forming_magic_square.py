#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
  
def formingMagicSquare(s):
    # Write your code here
    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]
    s = sum(s, [])
    # print(sum(s, []))
    minimum_cost = sys.maxsize

    # print(new_matrix)
    for mag in magic:
        diff = 0
        for i, j in zip(s, mag):
            abs_diff = abs( i-j)
            print(abs_diff)
            diff += abs_diff

        minimum_cost = min(minimum_cost, diff)
    print()
    print(minimum_cost)   
    return minimum_cost
    
    
params = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 5]]


result = formingMagicSquare(params)

assert result == 1
