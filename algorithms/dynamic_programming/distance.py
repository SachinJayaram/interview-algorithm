#!/usr/bin/env python


def edit_distance_dynamic_withspace(str1, str2):
    """!
    Time complexity O(m*n)
    Space Complexity O(m*n)
    """
    m = len(str1)
    n = len(str2)
    dp = [[0]*(n+1) for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])
    print(dp)

    return dp[m][n]


def edit_distance_recursion(str1, str2, m, n):
    """!
    Edit Distance using dynamic programming.
    Time Complexity O(3^m)
    """
    if not m:
        return n
    elif not n:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance_recursion(str1, str2, m-1, n-1)

    return 1 + min(edit_distance_recursion(str1, str2, m, n-1),
                   edit_distance_recursion(str1, str2, m-1, n),
                   edit_distance_recursion(str1, str2, m-1, n-1))


def ways_to_cover_distance(n):
    """!
    Using DP.

    Time complexity O(n)
    Space Complexity O(n)
    """
    dp = [0]*(n+1)
    dp[0] = 1
    if n > 1:
        dp[1] = 1
    if n > 2:
        dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


def ways_to_cover_distance_space(n):
    """!
    Using O(1) space.

    Time complexity O(n)
    Space Complexity O(1)
    """
    dp = [0]*3
    dp[0] = 1
    if n > 1:
        dp[1] = 1
    if n > 2:
        dp[2] = 2

    for i in range(3, n+1):
        dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3] + dp[(i-3)%3]

    return dp[n%3]
    

if __name__ == '__main__':
    str1 = 'saturday'
    str2 = 'sunday'
    print(edit_distance_dynamic_withspace(str1, str2))
    print(edit_distance_recursion(str1, str2, len(str1), len(str2)))
    print(ways_to_cover_distance(3))
    print(ways_to_cover_distance(4))
    print(ways_to_cover_distance_space(3))
    print(ways_to_cover_distance_space(4))
