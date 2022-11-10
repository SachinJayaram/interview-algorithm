#!/usr/bin/env python3

def factorial(n):
    if n == 0:
        return 1

    return n*factorial(n-1)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b

    return a

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def gcdi(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b

def main():
    # Factorial
    print("Factorial of 5 is {0}".format(factorial(5)))

    # Fib series: 0 1 1 2 3 5 8
    print("Fibonacci series till 6 is {0}".format(fib(6)))
    print("Fibonacci series till 7 is {0}".format(fibi(7)))

    # Gcd of a and b
    print("GCD of 24 and 9 is {0}".format(gcd(24, 9)))
    print("GCD of 24 and 12 is {0}".format(gcdi(24, 12)))


if __name__ == "__main__":
    main()