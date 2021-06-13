def coint_change(coin_array, s, n):
    if s == 0:
        return 1
    if n == 0:
        return 0
    
    if coin_array[n-1] <= s:
        return coint_change(coin_array, s, n-1) + coint_change(coin_array, s - coin_array[n-1], n)
    
    return coint_change(coin_array, s, n-1)


if __name__ == '__main__':
    coins = [4, 1, 2]
    s = 5
    ans = coint_change(coins, s, len(coins))
    print(ans)
