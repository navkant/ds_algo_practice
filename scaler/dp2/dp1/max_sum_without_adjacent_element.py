class Solution:
    def __init__(self):
        pass

    def max_sum_recurse(self, n, arr):
        if n <= 1:
            if n == 1:
                return max(arr[0], arr[1])
            else:
                return arr[0]

        return max(self.max_sum_recurse(n-1, arr),
                   self.max_sum_recurse(n-2, arr) + arr[n])

    def max_sum_iterative(self, arr):
        n = len(arr)

        dp = [0] * (n)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])

        return dp[-1]

    def solve(self, array):
        N = len(array)
        ans = self.max_sum_recurse(N-1, array)
        print(f'recursive ans is {ans}')

        ans2 = self.max_sum_iterative(array)
        print(f'itertive ans is {ans2}')


if __name__ == '__main__':
    obj = Solution()
    a = [5, 5, 10, 100, 10, 5]
    obj.solve(a)
