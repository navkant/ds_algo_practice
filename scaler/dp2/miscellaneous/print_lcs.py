class Solution:
    def lcs_dp(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        for row in dp:
            print(row)

        i = len(dp) - 1
        j = len(dp[0]) - 1
        ans = ''

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                ans = ans + str1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        return ans[::-1]

    def print_lcs(self, A, B):
        ans = self.lcs_dp(A, B)
        print(f'longest common subsequence is {ans}')


if __name__ == '__main__':
    a = 'abcdaf'
    b = 'acbcf'
    obj = Solution()
    obj.print_lcs(a, b)
