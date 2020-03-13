#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    sum = 0
    sum = x + y
    return sum


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    result = 0
    for _ in range(abs(y)):
        if y >= 0:
            result = add(result, x)
        else:
            result = add(result, -x)
    return result


def power(x, n):
    """Raise x to power n, where n >= 0"""
    power = 1
    for i in range(abs(n)):
        power = multiply(power, x) 
    return power


def factorial(x):
    """Compute factorial of x, where x > 0"""
    factorial = x
    if x <= 1:
        return 1
    else:
        while (x > 1):
            x -= 1
            factorial = multiply(factorial, x)
    return factorial

def fibonacci(n):
    result = 0
    firstNum = 0
    secNum = 1
    # for loop was here
    if n == 0: 
        result = 0 
    elif n==1: 
        result = 1
    elif n==2: 
        result = 1
    else:
        for _ in range(n-1):
            result = add(firstNum, secNum)
            firstNum = secNum
            secNum = result
    return result


if __name__ == '__main__':
    print(add(2, 4))
    print(multiply(5, 6))
    print(power(2, 3))
    print(factorial(6))
    print(fibonacci(8))
    pass
