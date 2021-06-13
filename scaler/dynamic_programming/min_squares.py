class Solution:
    # @param A : integer
    # @return an integer

    def countMinSquares(self, A):
        dp = [-1] * (A + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, A + 1):
            dp[i] = i

            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - (j * j)] + 1)
                j += 1

        print(dp)
        return dp[-1]


if __name__ == '__main__':
    a = 13
    obj = Solution()
    ans = obj.countMinSquares(a)


