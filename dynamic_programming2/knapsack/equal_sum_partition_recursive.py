def check_sum(arr, sum):
    if sum % 2 != 0:
        return False
    return subset_sum(arr, sum/2, len(arr))


def subset_sum(wt_array, sum, n):
    if sum == 0:
        return True

    if n == 0 or sum < 0:
        return False

    return subset_sum(wt_array, sum, n-1) or subset_sum(wt_array, sum - wt_array[n-1], n-1)


if __name__ == '__main__':
    weight_array = [1, 2, 4, 8, 15]
    sm =sum(weight_array)
    N = len(weight_array)
    ans = check_sum(weight_array, sm)
    if ans:
        print('Equal sum partition exists!!')
    else:
        print('Equal sum partition does not exists!!')
