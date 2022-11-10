#!/usr/bin/env python


def single_number(array):
    """!
    Get the number that occurs once in an array.
    Time complexity O(n*logn)
    Space Complexity O(1)
    """
    ones = 0
    twos = 0

    for i in range(len(array)):
        twos |= ones & array[i]
        ones ^= array[i]
        mask = ~(ones & twos)
        ones &= mask
        twos &= mask

    return ones


if __name__ == '__main__':
    print(single_number([3, 3, 2, 3, 1, 2, 2]))