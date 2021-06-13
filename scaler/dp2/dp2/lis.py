class Solution:
    # @param A : tuple of integers
    # @return an integer
    def __init__(self):
        self.maximum = -9999999999999

    def lis_recursive(self, array, n):
        if n == 1:
            return 1

        max_here = 1
        for i in range(n):
            result = self.lis_recursive(array, i)
            if array[i-1] < array[n-1] and result + 1 > max_here:
                max_here = result + 1

        self.maximum = max(self.maximum, max_here)
        return max_here

    def lis_iterative(self, array):
        n = len(array)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if array[j] < array[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
        return dp[-1]

    def solve(self, arr):
        n = len(arr)
        ans1 = self.lis_recursive(arr, n)
        print(f'recursive ans: {ans1}')
        ans2 = self.lis_iterative(arr)
        print(f'iterative ans is {ans2}')


if __name__ == "__main__":
    a = [22, 10, 9, 33, 21, 50, 41, 60]
    N = len(a)
    obj = Solution()
    ans = obj.solve(a)