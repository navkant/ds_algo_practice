class Solution:
    # @param A : integer
    # @return an integer
    def numTrees_recursive(self, A):
        if A == 0:
            return 1

        if A <=2:
            return A

        ans = 0
        for i in range(1, A+1):
            ans += self.numTrees_recursive(i-1) * self.numTrees_recursive(A-i)

        return ans

    def numTree_dp(self, A):
        dp = [0] * (A + 1)
        dp[0] = dp[1] = 1
        print(dp)
        for i in range(2, A+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        print(dp)
        return dp[-1]

    def numTrees(self, A):
        a = self.numTrees_recursive(A)
        print(f'recusrsive ans is {a}')
        b = self.numTree_dp(A)
        print(f'iterative ans is {b}')


if __name__ == '__main__':
    a = 4
    obj = Solution()
    obj.numTrees(a)
