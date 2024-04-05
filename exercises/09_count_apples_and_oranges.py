#!/bin/python3
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

from typing import List


def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]):
    total_apples = total_orange = 0

    for i in range(len(apples)):
        if s <= a + apples[i] <= t:
            total_apples += 1

    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            total_orange += 1
            
    print(total_apples)
    print(total_orange)
    return total_apples, total_orange
if __name__ == '__main__':

    s = 2
    t = 3
    a = 1
    b = 5
    apples = [2]
    oranges = [-2]
    
    total_apples, total_orange = countApplesAndOranges(s, t, a, b, apples, oranges)

    expected_a = 1
    expected_o = 1
    print(expected_a == total_apples)
    print(expected_o == total_orange)
