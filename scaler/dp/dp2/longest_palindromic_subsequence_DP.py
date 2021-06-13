class Solution:
    # @param A : string
    # @return an integer

    def check_palindrome_DP(self, string):
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for row in dp:
            print(row)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue
                print(i, j)
                if string[i] == string[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j],
                                   dp[i][j-1])
        print('   ', end='')
        for i in range(n):
            print(string[i], end=', ')
        print()
        for index, row in enumerate(dp):
            print(string[index], row)
        return dp[0][-1]

    def solve(self, A):
        n = len(A)
        return self.check_palindrome_DP(A)


if __name__ == '__main__':
    a = "abccba"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')