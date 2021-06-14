class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def isMatch_recurse(self, string, pattern, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1

            if j < 0:
                return 0

            if i < 0:
                if pattern[j] == '*' and self.isMatch_recurse(string, pattern, i, j-1):
                    return 1
                else:
                    return 0

        if pattern[j] == '?':
            return self.isMatch_recurse(string, pattern, i-1, j-1)
        if pattern[j] == '*':
            return self.isMatch_recurse(string, pattern, i-1, j) or self.isMatch_recurse(string, pattern, i, j-1)
        elif pattern[j] == string[i]:
            return self.isMatch_recurse(string, pattern, i-1, j-1)
        else:
            return 0

    def isMAtch_dp(self, string, pattern):
        m = len(pattern)
        n = len(string)

        dp = [[0 for j in range(n+1)] for i in range(2)]
        dp[0][0] = 1
        j = 0
        if pattern[0] == '*':
            dp[1][0] = 1

        for i in range(1, m+1):
            if pattern[i-1] == '*' and dp[0][0] == 1:
                dp[1][0] = 1
            else:
                pass

            for j in range(1, n+1):
                if pattern[i-1] == '?':
                    dp[1][j] = dp[0][j-1]
                elif pattern[i-1] == '*':
                    dp[1][j] = dp[0][j] or dp[1][j-1]
                elif pattern[i-1] == string[j-1]:
                    dp[1][j] = dp[0][j-1]
                else:
                    dp[1][j] = 0

            dp[0] = dp[1]
            dp[1] = [0] * (n+1)

        return dp[0][-1]

    def is_match_dp2(self, string, pattern):
        m = len(pattern)
        n = len(string)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = 1

        j = 0
        for i in range(1, m + 1):
            if pattern[i - 1] == '*' and dp[i - 1][j]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0

        for row in dp:
            print(row)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == string[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]

    def isMatch(self, A, B):
        m = len(A)
        n = len(B)
        return self.isMatch_recurse(A, B, m-1, n-1)

    def solve(self, string1, patt):
        ans = self.isMatch(string1, patt)
        print(f'recursive ans is {ans}')

        ans2 = self.is_match_dp2(string1, patt)
        print(f'iterative ans is {ans2}')


if __name__ == '__main__':
    a = ''
    b = '*****'
    obj = Solution()
    ans = obj.solve(a, b)
