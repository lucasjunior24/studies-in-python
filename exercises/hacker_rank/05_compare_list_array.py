#!/bin/python3

import os
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    alice = 0
    bob = 0
    for al in range(len(a)):
        if a[al] > b[al]:
            alice += 1
        elif a[al] < b[al]:
            bob += 1
    return [alice, bob]
    
    
if __name__ == '__main__':
    a = [5, 6, 7, 10]
    b = [5, 7, 4, 11]

    result = compareTriplets(a, b)
    print(result)
