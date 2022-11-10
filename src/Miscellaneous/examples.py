#!/usr/bin/env python

from collections import deque

def factorial(n):
    if n <= 0:
        return 1

    return n * factorial(n-1)

def get_number(a):
    return float(''.join([i for i in a if (i.isdigit() or i == '.')]))

def string_addition(a, b):
    return str(get_number(a) + get_number(b))

def move_zeroes_to_end(array):
    left_index = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[left_index], array[i], left_index = array[i], array[left_index], left_index + 1
    print(array)


def move_zeroes_to_end(array):
    """
    [1, 0, 2, 5, 0, 3, 0, 1, 2]
    """
    left_index = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i], array[left_index], left_index = array[left_index], array[i], left_index+1
    print(array)

def reverse_alpha(str_to_reverse):
    l = 0
    r = len(str_to_reverse) - 1
    str_to_reverse = [i for i in str_to_reverse]
    while l < r:
        if str_to_reverse[l].isalpha() and str_to_reverse[r].isalpha():
            str_to_reverse[l], str_to_reverse[r] = str_to_reverse[r], str_to_reverse[l]
            l, r = l+1, r-1
        elif not str_to_reverse[l].isalpha():
            l += 1
        elif not str_to_reverse[r].isalpha():
            r -= 1
    print(''.join(str_to_reverse))

def max_sub_array(array):
    max_sum = 0
    for i in range(1, len(array)):
        if array[i-1] > 0:
            array[i] += array[i-1]
        max_sum = max(max_sum, array[i])
    return max_sum

def longest_substring(s):
    queue = deque()
    char_dict = {}
    max_len = 0
    for char in s:
        if char in char_dict:
            cpop = None
            while cpop != char:
                cpop = queue.popleft()
                if cpop in char_dict:
                    char_dict.pop(cpop)
        queue.append(char)
        char_dict[char] = char
        max_len = max(max_len, len(queue))
    return max_len

def longest_substring1(s):
    stack = []
    max_len = 0
    for i in s:
        if i in stack:
            while i != stack.pop(0):
                continue
        stack.append(i)
        max_len = max(max_len, len(stack))
    return max_len

def solution(S, B):
    # write your code in Python 3.6
    C = []
    R = []
    for i in B:
        C.append(float(i))
    C.sort(reverse=True)
    for i in C[-1:]:
        R.append(f"{float(S)*(i/sum(C))}")
        S = S - R[-1]
        C.pop()

    return R

if __name__ == '__main__':
    print(factorial(5))
    n = 10
    print(string_addition("3.14", "2.2"))
    print(string_addition("100,000", "1"))
    move_zeroes_to_end([1, 0, 2, 5, 0, 0, 3])
    reverse_alpha('a,b$c')
    reverse_alpha('Ab,c,de!$')
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
    max_length = longest_substring("abcabcbb")
    print(f"longest substring in abcabcbb = {max_length}")
    max_length = longest_substring("bbbb")
    print(f"longest substring in abcabcbb = {max_length}")
    max_length = longest_substring1("pwwkew")
    print(f"longest substring in abcabcbb = {max_length}")
    print(solution('300.01', ['300.00', '200.00', '100.00']))