#!/usr/bin/env python
        
from typing import Collection
import collections

def coin_change(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, len(dp)):
            dp[i] = min(dp[i], dp[i-coin]+1)
            print(dp)
    return dp[amount] if dp[amount] < amount+1 else -1



def tournament(array, k):
    array_dict = collections.defaultdict(int)
    while True:
        if array[0] > array[1]:
            array[0], array[-1] = array[-1], array[0]
            array_dict[array[0]] += 1
            num = array[0]
        else:
            array[1], array[-1] = array[-1], array[0]
            array_dict[array[1]] += 1
            num = array[1]
        if array_dict[num] == k:
            return num


if __name__ == '__main__':
    print(coin_change([1, 2, 5], 11))
    print(tournament([2, 1, 3, 4, 5], 2))