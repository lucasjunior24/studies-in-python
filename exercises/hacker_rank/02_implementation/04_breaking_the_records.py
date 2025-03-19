#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    MIN_FIXED = sys.maxsize
    max_score = 0
    min_score = MIN_FIXED
    print(min_score)
    total_min = 0
    total_max = 0
    for score in scores:
        if score > max_score:
            if max_score > 0:
                total_max = total_max + 1
            max_score = score
            
        if score < min_score:
            if min_score < MIN_FIXED:
                total_min = total_min + 1
            min_score = score
            print(min_score)
    return [total_max, total_min]


result = breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42])
print(result)

assert result[0] == 4
assert result[1] == 0