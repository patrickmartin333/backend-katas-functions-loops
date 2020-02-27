#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "patrickmartin333"


def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    return x + y


print(add(2, 4))


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    # result = 0
    # for i in range(y):
    #     result += add(result, x)
    #
    # if x >= 0 or y >= 0:
    #     return result
    # else:
    #     return operator.neg(result)

    # I want to do this.. but can't seem to figure out how to incorporate my add function.. and it doesn't handle negative numbers
    result = 0
    for i in range(y):
        result += x
    return result


print(multiply(6, 88))


def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    if n == 0:
        return 1
    result = x
    increment = x
    for i in range(1, n):
        for j in range(1, x):
            result += increment
        increment = result
    return result


print(power(2, 8))


def factorial(x):
    """Compute factorial of x, where x > 0"""
    result = 1
    for i in range(1, x + 1):
        result += multiply(result, i)
    return result


factorial(4)


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here  --- Coming back to this..
    return


if __name__ == '__main__':
    # your code to call functions above
       """Docstring goes here"""
    print("Command line arguments: {}".format(sys.argv))
    # Invoke standalone main() with cmdline argument list.
    # Program should return status==0 if no errors.
    status = main(sys.argv)
    # return status code to OS.
    sys.exit(status)
    pass
