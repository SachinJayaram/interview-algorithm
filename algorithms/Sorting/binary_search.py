#!/usr/bin/env python


def binary_search_iterative(array, num):
    l = 0
    r = len(array) - 1
    while l <= r:
        mid = (l + r)//2
        if array[mid] == num:
            print("Number {0} for at {1}".format(num, mid))
            return mid
        elif array[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    print("Number {0} not found in the array".format(num))


def binary_search_rotated(array, l, r, num):
    if l > r:
        return -1

    mid = (l + r) // 2
    if array[mid] == num:
        print("Number {0} for at {1}".format(num, mid))
        return mid
    elif array[l] <= array[mid]:
        if array[l] <= num < array[mid]:
            return binary_search_rotated(array, l, mid-1, num)
        return binary_search_rotated(array, mid+1, r, num)
    elif array[mid] < num <= array[r]:
        return binary_search_rotated(array, mid+1, r, num)

    return binary_search_rotated(array, l, mid-1, num)

def bsr_iterative(array, num):
    l, r = 0, len(array)-1
    while l <= r:
        mid = (l+r)//2
        if array[mid] == num:
            print("Number {0} for at {1}".format(num, mid))
            return mid
        elif array[l] <= array[mid]:
            if array[l] <= num < array[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if array[mid] < num <= array[r]:
                l = mid + 1
            else:
                r = mid - 1
    print("Number {0} not found in the array".format(num))
    return -1


if __name__ == '__main__':
    array = [4, 7, 10, 15, 20, 40, 56, 75, 89, 100]
    binary_search_iterative(array, 101)
    array = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    l, r = 0, len(array) - 1
    binary_search_rotated(array, l, r, 3)
    binary_search_rotated(array, l, r, 5)
    binary_search_rotated(array, l, r, 9)
    binary_search_rotated(array, l, r, 10)
    binary_search_rotated(array, l, r, 7)
    binary_search_rotated(array, l, r, 2)
    binary_search_rotated(array, l, r, 4)
    bsr_iterative([4,5,6,7,0,1,2], 0)
    bsr_iterative([4,5,6,7,0,1,2], 3)
    bsr_iterative([3,1], 1)
    print(''.join([2, 3]))