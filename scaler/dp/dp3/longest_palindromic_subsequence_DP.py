class Solution:
    # @param A : string
    # @return an integer

    def check_palindromic_subsequence(self, string, i, j):
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue

                if string[i] == string[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j],
                                   dp[i][j-1])
        for row in dp:
            print(row)

        return dp[0][-1]

    def solve(self, A):
        return self.check_palindromic_subsequence(A, 0, len(A))


if __name__ == '__main__':
    a = "bebeeed"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')