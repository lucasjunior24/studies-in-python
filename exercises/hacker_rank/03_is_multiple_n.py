#!/bin/python3
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(numbes):
    # Write your code here
    for n in range(1, numbes + 1):

        is_m_3 = n % 3 == 0
        is_m_5 = n % 5 == 0
        if is_m_3 and is_m_5:
            print("FizzBuzz")
        elif is_m_3:
            print("Fizz")
        elif is_m_5:
            print("Buzz")
        else:
            print(n)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
