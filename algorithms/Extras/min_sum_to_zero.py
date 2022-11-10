#!/usr/bin/env python
        
def min_sum_to_zero(array):
    array.sort()
    l, r = 0, len(array) - 1
    min_sum = float('inf')
    while l < r:
        current_sum = array[l] + array[r]
        if current_sum < 0:
            l += 1
        else:
            r -= 1
        min_sum = min(min_sum, abs(current_sum))
    return min_sum


if __name__ == '__main__':
    print(min_sum_to_zero([1, 60, -10, 70, -80, 85]))