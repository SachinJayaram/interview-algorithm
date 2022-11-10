#!/usr/bin/env python


def magic_number(n):
    """!
    Get the nth magic number.
    Time complexity O(n*log(logn))
    Space Complexity O(n)
    """
    pow = 1
    output = 0
    while n:
        pow *= 5
        if n & 1:
            output += pow
        n >>= 1

    return output


if __name__ == '__main__':
    print(magic_number(3))
    print(magic_number(4))
    print(magic_number(5))
    print(magic_number(6))
    print(magic_number(7))
    print(magic_number(8))