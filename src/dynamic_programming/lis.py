#!/usr/bin/env python

def lis(arr):
    """!
    lis using dynamic programming.
    
    Time complexity O(n*n)
    Space Complexity O(n*n)
    """
    m = len(arr)
    arr_sorted = sorted(list(set(arr)))
    n = len(arr_sorted)

    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr[i-1] == arr_sorted[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lis_with_less_sapce(arr):
    """!
    lis using dynamic programming.
    
    Time complexity O(n*n)
    Space Complexity O(n)
    """
    n = len(arr)
    lookup = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lookup[i] < lookup[j] + 1:
                lookup[i] = lookup[j] + 1
    return max(lookup)


if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print("Length of lis is ", lis(arr))
