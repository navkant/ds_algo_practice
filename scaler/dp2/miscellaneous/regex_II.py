class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def ismatch_recursive(self, string, pattern, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 0

            if i < 0 and pattern[j] == '*':
                if self.ismatch_recursive(string, pattern, i, j-2):
                    return 1
                else:
                    return 0

        if string[i] == pattern[j] or pattern[j] == '.':
            return self.ismatch_recursive(string, pattern, i-1, j-1)
        if pattern[j] == '*':
            x1 = self.ismatch_recursive(string, pattern, i, j-2)
            x2 = False
            if string[i] == pattern[j-1]:
                x2 = self.ismatch_recursive(string, pattern, i-1, j)
            return x1 or x2
        else:
            return 0

    def ismatch_dp(self, string, pattern):
        m = len(pattern)
        n = len(string)
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = True

        for i in range(2, m+1):
            if pattern[i-1] == '*' and dp[i-2][0]:
                dp[i][0] = True
        for row in dp:
            print(row)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if pattern[i-1] == string[j-1] or pattern[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]

                if pattern[i-1] == '*':
                    x1 = dp[i-2][j]
                    x2 = False
                    if string[j-1] == pattern[i-2] or pattern[i-2] == '.':
                        x2 = dp[i][j-1]
                    dp[i][j] = x1 or x2
                else:
                    pass
        return dp[-1][-1]

    def isMatch(self, A, B):
        ans = self.ismatch_recursive(A, B, len(A)-1, len(B)-1)
        print(f'recursive ans is {ans}')
        ans = self.ismatch_dp(A, B)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = 'abbbc'
    b = 'ab*c'
    obj = Solution()
    obj.isMatch(a, b)