class Solution:
    # @param A : integer
    # @return an integer
    def recurse(self, A):
        if A <= 1:
            return 1

        return self.recurse(A - 1) + self.recurse(A - 2) * (A - 1)

    def solve(self, A):
        return self.recurse(A) % 10003

    # def solve(self, A):
    #     dp = [-1] * (A + 1)
    #
    #     dp[0] = 1
    #     dp[1] = 1
    #
    #     for i in range(2, A + 1):
    #         dp[i] = dp[i - 1] + dp[i - 2] * (i - 1)
    #
    #     print(dp)
    #     return dp[-1]


if __name__ == '__main__':
    a = 5
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
