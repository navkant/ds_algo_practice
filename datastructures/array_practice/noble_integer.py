
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def noble_integer(arr):
    # arr = list(set(arr))
    merge_sort(arr)
    print(arr)
    sol_found = False
    for i in range(len(arr)):
        # print(i == len(A) -1)
        if arr[i] == len(arr) - i - 1:
            print('sol found at ', i)
            sol_found = True
        elif arr[i] == 0 and i == len(arr) - 1:
            print('sol found at: ', i)
            sol_found = True
        else:
            continue

    if sol_found:
        return 1
    else:
        return -1

import array

