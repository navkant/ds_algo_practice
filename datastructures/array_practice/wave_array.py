def make_wave_array(A):
    A.sort()

    ans = []

    odds = A[1::2]
    evens = A[0::2]

    i = j = k = 0
    while i < len(odds) and j < len(evens):
        ans.append(odds[i])
        ans.append(evens[j])
        i += 1
        j += 1
        k += 1

    while i < len(odds):
        ans.append(odds[i])
        i += 1
        k += 1

    while j < len(evens):
        ans.append(evens[j])
        j += 1
        k += 1

    return ans
