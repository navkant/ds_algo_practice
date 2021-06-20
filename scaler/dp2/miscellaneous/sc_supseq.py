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
            print(f'i: {i} | j: {j}')
            if str1[i-1] == str2[j-1]:
                ans = ans + str1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    ans = ans + str1[i-1]
                    i -= 1
                else:
                    ans = ans + str2[j-1]
                    j -= 1
        if i >= 1:
            ans = ans + str1[:i][::-1]
        elif j >= 1:
            ans = ans + str2[:j][::-1]

        return ans[::-1]

    def sc_supseq(self, str1, str2):
        sc_supseq = self.lcs_dp(str1, str2)
        print(f'ans is {sc_supseq}')


if __name__ == '__main__':
    a = "abac"
    b = "cab"
    c = 'aaaaaaaaa'
    obj = Solution()
    obj.sc_supseq(a, b)
