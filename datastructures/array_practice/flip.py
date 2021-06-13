def flip(arr):
    print(arr)
    ans = [-1, -1]
    diff = 0
    imax = 0
    start = 0
    sol_found = False
    for i in range(len(arr)):
        if arr[i] == '0':
            diff += 1
        else:
            diff += -1

        if diff < 0:
            diff = 0
            start = i + 1

        if imax < diff:
            imax = diff
            ans[0] = start
            ans[1] = i
            sol_found = True

    if not sol_found:
        return []

    # ans[0] += 1
    # ans[1] += 1
    print(arr[ans[0]: ans[1] + 1])
    return ans


def flip2(arr):
    print(arr)
    diff = 0
    imax = 0
    start = 0
    sol_found = False
    ans = [-1, -1]
    for i in range(len(arr)):
        if arr[i] == '0':
            diff += 1
        else:
            diff += -1

        if diff < 0:
            diff = 0
            start = i + 1

        if imax < diff:
            imax = diff
            ans[0] = start
            ans[1] = i
            sol_found = True

    if not sol_found:
        return []
    print(arr[ans[0]:ans[1] + 1])
    return ans
