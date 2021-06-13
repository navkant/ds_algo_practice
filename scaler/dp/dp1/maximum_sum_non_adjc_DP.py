import sys

class Solution:
    # @param A : tuple of integers
    # @return an integer
    # def __init__(self):
    #     self.ans = sys.maxsize * -1

    def maximum_sum_non_adjc(self, arr):
        n = len(arr)
        dp = [0] * n

        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + arr[i])

        return dp[-1]


if __name__ == '__main__':
    a = [2, 3, 5, 0, 7, 10]
    obj = Solution()
    ans = obj.maximum_sum_non_adjc(a)
    print(f'ans is {ans}')
