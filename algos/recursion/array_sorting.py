def sort_array(array):
    if len(array) == 1:
        return array
    else:
        pass
    last_element = array[-1]
    array = array[:-1]
    array = sort_array(array)
    array = put_element_in_array(array, last_element)
    return array


def put_element_in_array(arr, val):
    if len(arr) == 0 or arr[-1] <= val:
        arr.append(val)
        return arr
    last_element = arr[-1]
    arri = arr[:-1]
    arri = put_element_in_array(arri, val)
    arri.append(last_element)
    return arri


if __name__ == '__main__':
    arr = [9, 8, 7, 6, 5, 4, 3]  # unsorted 3, 4, 6, 7, 5, 8, 9]
    a = sort_array(arr)
    print(a)
