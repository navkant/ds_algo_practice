class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def is_match_recurse_DP(self, text, patt):
        m = len(text)
        n = len(patt)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = 1

        j = 0
        for i in range(1, n+1):
            if patt[i - 1] == '*' and dp[i-1][j]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

        for row in dp:
            print(row)

        for i in range(1, n+1):
            for j in range(1, m+1):
                print(f'i: {i} j: {j}')
                if patt[i-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif patt[i-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif patt[i-1] == text[j-1]:
                    dp[i][j] = 1 and dp[i-1][j-1]
                else:
                    dp[i][j] = 0

        for row in dp:
            print(row)
        return dp[-1][-1]

    def isMatch(self, A, B):
        x = len(A)
        y = len(B)
        return self.is_match_recurse_DP(A, B )


if __name__ == '__main__':
    a = 'acz'
    b = 'a?a'
    obj = Solution()
    ans = obj.isMatch(a, b)
    print(f'ans is {ans}')
