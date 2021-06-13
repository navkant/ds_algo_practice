def subset_sum(wt_array, sum, n):
    if sum == 0:
        return True
    if n == 0:
        return False
    
    if wt_array[n-1] > sum:
        return subset_sum(wt_array, sum, n-1)
    
    return subset_sum(wt_array, sum, n-1) or subset_sum(wt_array, sum - wt_array[n-1], n-1)


if __name__ == '__main__':
    weight_array = [3, 5, 6, 8, 10]
    SUM = 11
    ans = subset_sum(weight_array, SUM, len(weight_array))
    print(ans)
