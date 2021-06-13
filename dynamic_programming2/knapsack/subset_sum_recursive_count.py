def subsetsum(arr, sum, n):
    if sum == 0:
        return 1
    if n == 0:
        return 0

    if arr[n-1] > sum:
        return subsetsum(arr, sum, n-1)
    
    return subsetsum(arr, sum, n-1) + subsetsum(arr, sum - arr[n-1], n-1)


if __name__ == '__main__':
    weight_array = [1, 3, 5, 6, 8, 10]
    SUM = 11
    ans = subsetsum(weight_array, SUM, len(weight_array))
    print(ans)
