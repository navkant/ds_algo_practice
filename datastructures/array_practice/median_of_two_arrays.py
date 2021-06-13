def median(arr1, arr2):
    if len(arr2) == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    if len(arr1) % 2 == 0:
        middle2 = len(arr2) // 2
        middle1 = middle2 - 1
        print(f'middle1: {middle1}   middle2: {middle2}')
        m1 = (arr1[middle1] + arr1[middle2]) / 2
        m2 = (arr2[middle1] + arr2[middle2]) / 2
        if m1 > m2:
            return median(arr1[:middle2], arr2[middle2:])
        else:
            return median(arr1[middle2:], arr2[:middle2])
    else:
        middle = len(arr1) // 2
        m1 = arr1[middle]
        m2 = arr2[middle]
        if m1 > m2:
            return median(arr1[:middle+1], arr2[middle:])
        else:
            return median(arr1[middle:], arr2[:middle+1])


if __name__ == '__main__':
    a1 = [1, 12, 15]  #  , 26]  # , 38]
    a2 = [2, 13, 17]  #  , 30]  # , 45]

    ans = median(a1, a2)
    print(f'median is {ans}')
