class Solution:
    # @param A : integer
    # @return an integer
    def count_trees_recursively(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1

        ans = 0
        for i in range(1, n+1):
            ans += self.count_trees_recursively(i-1) * self.count_trees_recursively(n-i)

        return ans

    def count_trees_iterative(self, n):
        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]

        return dp[-1]

    def numTrees(self, A):
        ans1 = self.count_trees_recursively(A)
        print(f'recursive ans is {ans1}')
        ans2 = self.count_trees_iterative(A)
        print(f'iterative ans is {ans2}')


if __name__ == '__main__':
    x = 5
    obj = Solution()
    obj.numTrees(x)