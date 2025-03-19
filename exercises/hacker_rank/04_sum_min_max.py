#!/bin/python3
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    x = sum(arr)
    without_less = x - min(arr)
    without_more =  x - max(arr)
    print(without_more, without_less) 

if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]

    miniMaxSum(arr)