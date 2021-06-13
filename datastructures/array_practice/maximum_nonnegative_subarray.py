import sys


def maxset(arr):
    array_list = []
    sub_array = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            sub_array.append(arr[i])
        else:
            array_list.append(sub_array)
            sub_array = []

    array_list.append(sub_array)
    print(array_list)
    max_sum = -sys.maxsize
    ret_arr = []
    for i in array_list:
        if sum(i) > max_sum:
            max_sum = sum(i)
            ret_arr = i

    return ret_arr
