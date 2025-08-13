def isPowerOfThree(n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


input = 27

output = isPowerOfThree(input)
expect = True

if output == expect:
    print("Done")
else:
    print("Failed")
