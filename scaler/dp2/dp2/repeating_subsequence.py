class Solution:
    def lcs_iterative(self, string1, string2):
        m = len(string1)
        n = len(string2)

        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for row in dp:
            print(row)
        print()

        for i in range(1, n+1):
            for j in range(1, m+1):
                if string2[i-1] == string1[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],
                                   dp[i][j-1])
        for row in dp:
            print(row)
        return dp[-1][-1]

    def lcs_recursive(self, string1, string2, m, n):
        if m < 0 or n < 0:
            return 0

        if string1[m] == string2[n] and m != n:
            return 1 + self.lcs_recursive(string1, string2, m-1, n-1)
        else:
            return max(self.lcs_recursive(string1, string2, m-1, n),
                       self.lcs_recursive(string1, string2, m, n-1))

    def solve(self, str1):
        a = len(str1)
        ans1 = self.lcs_recursive(str1, str1, a-1, a-1)
        print(f'recursive ans is {ans1}')
        ans2 = self.lcs_iterative(str1, str1)
        print(f'iterative ans is {ans2}')


if __name__ == '__main__':
    a = 'abcdbapolkmcqwp'
    obj = Solution()
    obj.solve(a)
