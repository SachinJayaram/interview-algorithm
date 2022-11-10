#!/usr/bin/env python


def get_prime_numbers(n):
    """!
    Get the prime numbers upto n.
    Time complexity O(n*log(logn))
    Space Complexity O(n)
    """
    primes = [True for i in range(n+1)]
    p = 2
    while p*p <= n:
        if primes[p]:
            for i in range(p*p, n+1, p):
                primes[i] = False
        p += 1

    return [i for i in range(2, len(primes)) if primes[i]]


if __name__ == '__main__':
    print(get_prime_numbers(50))