class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def longest_common_subsequence_DP(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],
                                   dp[i][j-1])

        return dp[-1][-1]

    def solve(self, A, B):
        return self.longest_common_subsequence_DP(A, B)


if __name__ == '__main__':
    a = 'abbcdgf'
    b = 'bbadcgf'
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
