#!/bin/python3

import os


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def timeConversion(s):
    # Write your code here
    hour = s[:-2]
    type_hour = s[-2:]
    if(type_hour == "PM"):
        if hour[:2] == "12":
            return hour
        new_hour = str(int(hour[:2]) + 12) + hour[-6:]
        return new_hour
    else:
        if hour[:2] == "12":
            return "00" + hour[-6:]
        return hour
    

if __name__ == '__main__':

    # n = int(input().strip())

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    result = timeConversion("07:05:45PM")
    print(result)