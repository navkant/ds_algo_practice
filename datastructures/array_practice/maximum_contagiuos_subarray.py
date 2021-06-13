import sys


def maximum_sum_subarray(A):
    ans = 0
    curr_sum = 0
    if len(A) == 1:
        return A[0]
    for i in range(len(A)):
        if curr_sum + A[i] > 0:
            curr_sum += A[i]
        else:
            curr_sum = 0
        ans = max(ans, curr_sum)

    return ans


def max_sum_subarray(A, low, high):
    if n == 1:
        return A[0]
    m = (high - low) / 2
    left_MSS = Max_sum_subarray(A, low, m)
    right_MSS = Max_sum_subarray(A, m, high)
    left_sum = -sys.maxsize
    right_sum = -sys.maxsize
    curr_sum = 0
    for i in range(low, m):
        curr_sum += A[i]
        left_sum = max(left_sum, curr_sum)
    curr_sum = 0
    for i in range(m, high):
        curr_sum += A[i]
        right_sum = max(right_sum, curr_sum)

    return max(left_MSS, right_MSS, left_sum+right_sum)
