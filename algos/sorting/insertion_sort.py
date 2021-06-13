def insertion_sort(arr1):
    for i in range(len(arr1)):
        for j in range(i+1, len(arr1)):
            if arr1[j] < arr1[i]:
                arr1[i], arr1[j] = arr1[j], arr1[i]     # swap elements
    return arr1


if __name__ == "__main__":
    arr = [4, 6, 3, 2, 1, 9, 7]
    arr = insertion_sort(arr)
    print(arr)
