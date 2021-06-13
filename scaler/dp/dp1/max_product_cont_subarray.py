class Solution:
    # @param A : tuple of integers
    # @return an integer

    def max_prodct_recurse(self, arr):
        n = len(arr)

        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = arr[0]
        dp2[0] = arr[0]

        for i in range(1, n):
            minn = min(arr[i], dp1[i-1] * arr[i], dp2[i-1] * arr[i])
            maxx = max(arr[i], dp1[i-1] * arr[i], dp2[i-1] * arr[i])
            dp1[i] = minn
            dp2[i] = maxx

        print(dp1)
        print(dp2)

        return max(dp2)


if __name__ == '__main__':
    a = [1, 4, -2, 2, -5, 1]
    n = len(a)
    obj = Solution()
    ans = obj.max_prodct_recurse(a)
    print(f'ans is {ans}')
