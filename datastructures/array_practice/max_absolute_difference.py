import sys


def max_absolute_diff(arr):
    max1 = -sys.maxsize
    min1 = +sys.maxsize

    max2 = -sys.maxsize
    min2 = +sys.maxsize

    for i in range(len(arr)):
        max1 = max(max1, arr[i] + i)
        min1 = min(min1, arr[i] + i)

        max2 = max(max2, arr[i] - i)
        min2 = min(min2, arr[i] - i)

    return max((max1 - min1), (max2 - min2))
