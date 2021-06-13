def subset_sum(wt_array, sum, n):
    if sum == 0:
        return True
    if n == 0:
        return False
    
    if wt_array[n-1] > sum:
        return subset_sum(wt_array, sum, n-1)
    
    return subset_sum(wt_array, sum, n-1) or subset_sum(wt_array, sum - wt_array[n-1], n-1)


def min_subset_diff(arr, diff):
    possible_sums = list()
    for i in range(sum(arr)//2):
        if subset_sum(arr, i, len(arr)):
            possible_sums.append(i)
    count = 0
    for i in possible_sums:
        if (sum(arr) - (2 * i)) == diff:
            count += 1
        else:
            pass
    return count


if __name__ == '__main__':
    weight_array = [1, 3, 6, 14]
    sm =sum(weight_array)
    N = len(weight_array)
    diff = 4
    ans = min_subset_diff(weight_array, diff)
    print('Number of subsets with diff {} is: {}'.format(diff, ans))
