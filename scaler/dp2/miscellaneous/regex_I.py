class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def regex_match_recursive(self, string, pattern, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 0
            if i < 0 and pattern[j] == '*' and self.regex_match_recursive(string, pattern, i, j - 1):
                return 1
            else:
                return 0

        if string[i] == pattern[j] or pattern[j] == '?':
            return self.regex_match_recursive(string, pattern, i - 1, j - 1)
        elif pattern[j] == '*':
            return self.regex_match_recursive(string, pattern, i - 1, j) or self.regex_match_recursive(string, pattern, i, j - 1)
        else:
            return 0

    def regex_match_dp(self, string, pattern):
        m = len(string)
        n = len(pattern)

        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = 1

        for j in range(1, n + 1):
            if pattern[j - 1] == '*' and dp[0][j - 1]:
                dp[0][j] = 1

        for row in dp:
            print(row)
        print()
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if string[i - 1] == pattern[j - 1] or pattern[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]

                if pattern[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        for row in dp:
            print(row)
        return dp[-1][-1]

    def isMatch(self, A, B):
        # return self.regex_match_recursive(A, B, len(A)-1, len(B)-1)
        ans = self.regex_match_dp(A, B)
        print(f'ans is {ans}')


if __name__ == '__main__':
    a = ''
    b = '*****'
    obj = Solution()
    obj.isMatch(a, b)