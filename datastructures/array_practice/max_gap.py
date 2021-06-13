def max_gap(A):
    n = len(A)

    hash_map = {}
    for i, v in enumerate(A):
        if v not in hash_map:
            hash_map[v] = [i]
        else:
            hash_map[v].append(i)
    A.sort(reverse=False)
    diff = 0
    temp = len(A)
    for i in range(len(A)):
        if temp > hash_map[A[i]][0]:
            temp = hash_map[A[i]][0]
        diff = max(diff, hash_map[A[i]][-1] - temp)
    return diff
