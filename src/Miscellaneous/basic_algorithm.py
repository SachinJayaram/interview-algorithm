#!/usr/bin/env python

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fib(n-1) + fib(n-2)

def fib_sequence(n):
    fib_array = []
    for i in range(n):
        fib_array.append(fib(i))

    print(fib_array)

def fib_with_mem(n, array):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif array[n] > 0:
        return array[n]
    
    array[n] = fib_with_mem(n-1, array) + fib_with_mem(n-2, array)

def fib_with_mem(n, fib_array):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif fib_array[n] > 0:
        return fib_array[n]
    fib_array[n] = fib_with_mem(n-1, fib_array) + fib_with_mem(n-2, fib_array)

def fib_seq_with_mem(n):
    fib_array = [0]*n
    if n < 2:
        return fib_array
    for i in range(2, n):
        fib_with_mem(i, fib_array)
    return fib_array

def can_place_flowers(flowerbed, n):
    if not n:
        return True
    i = 0
    f = [0] + flowerbed + [0]
    while i < len(f) - 1:
        if f[i-1] == f[i] == f[i+1]:
            n -= 1
            if not n:
                return True
            i += 2
        else:
            i += 1
    return False

def find_word(array):
    """
    in, pa, ai, sp
    ain, pa, sp
    in, ai, pa, sp
    in, ain, pa, sp
    pain, sp
    spain
    pe, ru, er
    per, 
    """
    word_dict = {}
    for kv in array:
        k, v = kv.split(">")
        word_dict[k] = v
def main():
    print(factorial(4))
    fib_sequence(10)
    print(fib_seq_with_mem(10))
    print(fib_seq_with_mem(0))
    print(fib_seq_with_mem(1))

if __name__ == '__main__':
    main()