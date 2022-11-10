#!/usr/bin/env python

import heapq

def bubble_sort(array):
    """!
    Sort an array using bubble sort.
    
    Time complexity O(n*n)
    Space Complexity O(1)
    """
    print('sorting using bubble sort')
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)

def selection_sort(array):
    """!
    Sort an array using selection sort.
    
    Time complexity O(n*n)
    Space Complexity O(1)
    """
    print('sorting using selection sort')
    array_len = len(array)
    for i in range(array_len):
        min_index = i
        for j in range(i+1, array_len):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)    

def insertion_sort(array):
    """!
    Sort an array using insertion sort.
    
    Time complexity O(n*n)
    Space Complexity O(1)
    """
    print('sorting using insertion sort')
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    print(array)

def merge_sort(array):
    """!
    Sort an array using merge sort.
    
    Time complexity O(n*logn)
    Space Complexity O(n)
    """
    if len(array) <= 1:
        return None
    mid = len(array) // 2
    l = array[:mid]
    r = array[mid:]
    merge_sort(l)
    merge_sort(r)
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            array[k] = l[i]
            i += 1
        else:
            array[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        array[k] = l[i]
        i, k = i+1, k+1
    while j < len(r):
        array[k] = r[j]
        j, k = j+1, k+1
    
    return array

def partition(array, l, r):
    """!
    Take the last element as pivot and place it at 
    its correct position in sorted array. All smaller
    elements are placed to the left of pivot and vice
    versa.
    """
    j = l - 1
    pivot = array[r]
    for i in range(l, r):
        if array[i] <= pivot:
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j+1], array[r] = array[r], array[j+1]
    
    return j + 1

def quick_sort(array, l, r):
    """!
    Sort an array using quick sort.
    
    Time complexity O(n*logn) (Best, Average), O(n*n) (Worst case).
    Space Complexity O(n)
    """
    if len(array) <= 1:
        return None
    if l < r:
        pi = partition(array, l, r)
        quick_sort(array, l, pi-1)
        quick_sort(array, pi+1, r)

    return array

def heap_sort(array):
    print('sorting using heap sort')
    heap = []
    for i in array:
        heapq.heappush(heap, i)
    return [heapq.heappop(heap) for _ in range(len(heap))]

if __name__ == '__main__':
    bubble_sort([12, 11, 13, 5, 6])
    selection_sort([12, 11, 13, 5, 6])
    insertion_sort([12, 11, 13, 5, 6])
    print('sorting using merge sort')
    print(merge_sort([12, 11, 13, 5, 6]))
    print('sorting using quick sort')
    array = [10, 7, 8, 9, 1, 5]
    print(quick_sort(array, 0, len(array)-1))
    print(heap_sort([12, 11, 13, 5, 6]))