#!/bin/python3
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    # Write your code here
    max_score = min_score = scores[0]
    print(min_score)
    max_count = min_count = 0
    for score in scores:
        if min_score < score:
            min_count += 1
            min_score = score

        elif max_score > score:
            max_count += 1
            max_score = score
            
    return [min_count, max_count]

params = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = breakingRecords(params)
print(result)

assert result[0] == 4
assert result[1] == 0