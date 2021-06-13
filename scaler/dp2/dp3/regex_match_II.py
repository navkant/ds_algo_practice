class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def is_match_recursive(self, string, pattern, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 0
            if i < 0:
                if pattern[j] == '*' and self.is_match_recursive(string, pattern, i, j-2):
                    return 1
                else:
                    return 0

        if string[i] == pattern[j] or pattern[j] == '.':
            return self.is_match_recursive(string, pattern, i-1, j-1)
        elif pattern[j] == '*':
            x = self.is_match_recursive(string, pattern, i, j-2)
            print(f'i: {i} j: {j} x: {x}')
            if string[i] == pattern[j-1] or pattern[j-1] == '.':
                return x or self.is_match_recursive(string, pattern, i-1, j)
            else:
                return x
        else:
            return 0

    def is_match_dp(self, string, pattern):
        m = len(string)
        n = len(pattern)

        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = 1

        for j in range(2, n+1):
            if pattern[j-1] == '*' and dp[0][j-2]:
                dp[0][j] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if string[i-1] == pattern[j-1] or pattern[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j-1] == '*':
                    if pattern[j-2] == string[i-1] or pattern[j-2] == '.':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]

    def is_math_dp2(self, string, pattern):
        m = len(pattern)
        n = len(string)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dp[0][0] = 1

        for i in range(2, m + 1):
            if pattern[i - 1] == '*' and dp[i - 2][0]:
                dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[i - 1] == '*':
                    if pattern[i - 2] == string[j - 1] or pattern[i - 2] == '.':
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]
            else:
                dp[i][j] = 0

        return dp[-1][-1]

    def isMatch(self, A, B):
        m = len(A)
        n = len(B)

        ans = self.is_match_recursive(A, B, len(A) - 1, len(B) - 1)
        print(f'recursive ans is {ans}')
        ans = self.is_match_dp(A, B)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    A = "a"
    B = "a"
    obj = Solution()
    obj.isMatch(A, B)
