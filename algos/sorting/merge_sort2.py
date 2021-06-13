def merge_sort(array, low, high):
    if len(array) > 1:
        mid = low + ((high - low) / 2)

        merge_sort(array, low, mid+1)
        merge_sort(array, mid, high)

        i = low
        j = mid

        while (i < mid) and (j < high):
            

    


if __name__ == '__main__':
    arr = [4, 6, 3, 2, 1, 9, 7]
    arr = insertion_sort(arr)
    print(arr)