from functools import cache

coins = [1, 2, 5, 10, 20, 50, 100, 200]

@cache
def count_ways(amount, i=0):
    if amount == 0: return 1
    if amount < 0 or i == len(coins): return 0
    
    with_coin = count_ways(amount - coins[i], i)
    without_coin = count_ways(amount, i + 1)
    
    return with_coin + without_coin

print(count_ways(200))