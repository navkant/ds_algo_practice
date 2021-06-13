class Solution:
    def is_interleave_recursive(self, str1, str2, str3, m, n, result, i, j):
        if i >= m and j >= n:
            if result == str3:
                return 1

        ans = False
        if i < m:
            ans |= self.is_interleave_recursive(str1, str2, str3, m, n, result+str1[i], i+1, j)
        if j < n:
            ans |= self.is_interleave_recursive(str1, str2, str3, m, n, result+str2[j], i, j+1)
        return ans

    def is_iterative_memoized(self, str1, str2, str3, m, n, i, j, k, dp):
        if i == m:
            return str2[j:] == str3[k:]
        if j == n:
            return str1[i:] == str3[k:]

        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        x1 = str1[i] == str3[k] and self.is_iterative_memoized(str1, str2, str3, m, n, i+1, j, k+1, dp)
        x2 = str2[j] == str3[k] and self.is_iterative_memoized(str1, str2, str3, m, n, i, j+1, k+1, dp)

        if x1 or x2:
            ans = 1

        dp[i][j] = ans
        return ans

    def is_interleave_dp(self, str1, str2, str3):
        m = len(str1)
        n = len(str2)
        dp = [[False for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and str2[j-1] == str3[i+j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and str1[i-1] == str3[i+j-1]
                else:
                    dp[i][j] = (dp[i-1][j] and str1[i-1] == str3[i+j-1]) or (dp[i][j-1] and str2[j-1] == str3[i+j-1])

        return dp[-1][-1]

    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)

        ans = self.is_interleave_recursive(s1, s2, s3, m, n, '', 0, 0)
        print(f'recursive ans is {ans}')

        dp = [[-1 for j in range(n)] for i in range(m)]
        ans = self.is_iterative_memoized(s1, s2, s3, m, n, 0, 0, 0, dp)
        print(f'iterative ans is {ans}')

        ans = self.is_interleave_dp(s1, s2, s3)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = "abc"
    b = "def"
    c = "dabecf"
    obj = Solution()
    obj.isInterleave(a, b, c)
