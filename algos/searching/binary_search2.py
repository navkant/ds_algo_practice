def binary_search(array, key):
    N = len(arr)
    low = 0
    high = N - 1
    while low <= high:
        mid = low + (high-low) // 2
        if array[mid] > key:
            high = mid - 1
        elif array[mid] == key:
            return mid
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 6, 7, 9]
    start = 0
    end = len(arr) - 1
    arr = binary_search(arr, 77)
    print(arr)
