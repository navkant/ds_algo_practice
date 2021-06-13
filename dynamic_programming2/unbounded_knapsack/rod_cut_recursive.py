def knapsack(length_array, price_array, cap, n):
    print(f'cap: {cap} n: {n} ')
    if cap == 0 or n == 0:
        print('exit')
        return 0
    if length_array[n-1] <= cap:
        take = price_array[n-1] + knapsack(length_array, price_array, cap - length_array[n-1], n)
        not_take = knapsack(length_array, price_array, cap, n-1)
        print(f'take: {take}  not_take: {not_take}')
        ans = max(take, not_take)
        return ans
    else:
        return knapsack(length_array, price_array, cap, n-1)


if __name__ == "__main__":
    length_array = [1, 2, 3, 4, 5, 6, 7, 8]
    price_array = [2, 3, 4, 5, 6, 7, 8, 9]
    capacity = 8
    profit = knapsack(length_array, price_array, capacity, len(length_array))
    print(profit)
