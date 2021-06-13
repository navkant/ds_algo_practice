def binary_search(array, key, start, end):
    if end - start == 1:
        if array[start] == key:
            return start
        elif array[end] == key:
            return end
        else:
            return -1

    mid = (start + end) // 2
    print(f'start: {start}, mid: {mid},  end: {end}')
    if array[mid] == key:
        print('found at mid: ', mid)
        return mid
    elif array[mid] > key:
        return binary_search(array, key, start, mid)
    elif array[mid] < key:
        return binary_search(array, key, mid, end)


def main(arr, key):
    start = 0
    end = len(arr)
    ans = binary_search(arr, key, start, end)
    return ans
