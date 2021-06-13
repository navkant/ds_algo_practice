def triplet_with_sum_in_range(arr, a=1, b=2):
    arr = list(map(float, arr))
    n = len(arr)
    arr.sort()
    k = n
    print(f'arr: {arr}')

    for i in range(n-2):
        j = i + 1
        k = n-1
        while j != k:
            sum = arr[i] + arr[j] + arr[k]
            if sum < a and sum < b:
                j += 1
                continue
            elif a < sum < b:
                print(f'a[i]: {arr[i]}, a[j]: {arr[j]}, a[k]: {arr[k]}')
                print(f'sum: {sum}')
                return 1
            elif sum > a and sum > b:
                print(f'sum: {sum}')
                k += -1
