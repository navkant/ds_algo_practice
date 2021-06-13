def coint_change(coin_array, s, n, cc):
    if s == 0:
        return min(cc, len(coin_array) - n)
    if n == 0:
        return

    if coin_array[n-1] <= s:
        return min(coint_change(coin_array, s, n-1, cc), coint_change(coin_array, s - coin_array[n-1], n, cc))

    return coint_change(coin_array, s, n-1, cc)


if __name__ == '__main__':
    coins = [1, 2, 3]
    s = 5
    coins_count = 999999
    ans = coint_change(coins, s, len(coins), coins_count)
    print(ans)
