#!/bin/python3


import os


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1: int, v1: int, x2: int, v2: int):
    POS_MAX = 10000
    JUMP_MAX = 10000
    
    if ((1 <= v1 and v1 <= JUMP_MAX and 1 <= v2 and v2 <= JUMP_MAX) == False):
        return "NO"
    while True:

        if (0 <= x1 and x1 <= x2 and x2 <= POS_MAX):
            if (x1 == x2):
                return "YES"
            else:
                x1 += v1
                x2 += v2
                continue
        break
    # Write your code here
    return "NO"
    # Write your code here

if __name__ == '__main__':

    x1 = int(0)

    v1 = int(3)

    x2 = int(5)

    v2 = int(2)
 
    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
