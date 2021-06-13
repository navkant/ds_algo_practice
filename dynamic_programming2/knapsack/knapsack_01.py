def knapsack(wt_array, val_array, cap, n):
    if cap == 0 or n == 0:
        return 0
    if wt_array[n-1] <= cap:
        return max(val_array[n-1] + knapsack(wt_array, val_array, cap - wt_array[n-1], n-1), knapsack(wt_array, val_array, cap, n-1))
    else:
        return knapsack(wt_array, val_array, cap, n-1)


if __name__ == "__main__":
    weight_array = [1, 2, 3, 4]
    value_array = [2, 4, 5, 7]
    capacity = 7
    profit = knapsack(weight_array, value_array, capacity, 4)
    print(profit)
