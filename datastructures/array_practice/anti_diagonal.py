def anti_diagonal(A):
    n = len(A[0])

    x = 0
    y = 0
    return_array = []
    for i in range(n):
        x = i
        sub_array = []
        for j in range(i+1):
            y = j
            # print(A[y][x], end=' ')
            sub_array.append(A[y][x])
            x += -1
            y += 1
        print('')
        return_array.append(sub_array)

    for i in range(1, n):
        x = i
        # print('x', x)
        sub_array = []
        for j in range(n-1, 0, -1):
            if x == n:
                break
            y = j
            # print('y', y)
            # print(A[x][y], end=' ')
            sub_array.append(A[x][y])
            x += 1
            y += -1
        print('')
        return_array.append(sub_array)
    return return_array
