def solve(n, k):
    if k > (2 ** (n-1)):
        return 'Invalid input'
    if n == 1 and k == 1:
        return 0
    mid = (2 ** (n-1)) / 2

    if k <= mid:
        return solve(n-1, k)
    elif k > mid:
        x = solve(n-1, k-mid)
        return int(not x)


if __name__ == '__main__':
    ans = solve(2,2)
    print('ans is: ', ans)
