def insertion_sort(arr1):
    for i in range(1, len(arr1)):
        value = arr1[i]
        j = i - 1
        while arr1[j] > value and j >= 0:
            arr1[j+1] = arr1[j]
            j -= 1
        arr1[j+1] = value
    return arr1


if __name__ == "__main__":
    arr = [4, 6, 3, 2, 1, 9, 7]
    arr = insertion_sort(arr)
    print(arr)
