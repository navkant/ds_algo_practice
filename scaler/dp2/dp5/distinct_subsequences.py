class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def numDistinct_recursive(self, str1, str2, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 1
            else:
                return 0

        if str1[i] == str2[j]:
            return self.numDistinct_recursive(str1, str2, i-1, j-1) + self.numDistinct_recursive(str1, str2, i-1, j)

        return self.numDistinct_recursive(str1, str2, i-1, j)

    def numDistinct_dp(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[-1][-1]

    def numDistinct(self, A, B):
        ans = self.numDistinct_recursive(A, B, len(A)-1, len(B)-1)
        print(f'recursive ans is {ans}')
        ans = self.numDistinct_dp(A, B)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = 'rabbbit'
    b = 'rabbit'
    obj = Solution()
    obj.numDistinct(a, b)