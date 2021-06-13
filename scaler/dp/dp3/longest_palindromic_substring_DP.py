class Solution:
    # @param A : string
    # @return an integer

    def check_palindromic_substring(self, string, i, j):
        n = len(string)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue
                if i+1 == j and string[i] == string[j]:
                    dp[i][j] = True

                elif string[i] == string[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

        for row in dp:
            print(row)

        maxx = 1
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if dp[i][j]:
                    maxx = max(maxx, j - i + 1)

        print(maxx)
        return dp[0][-1]

    def solve(self, A):
        return self.check_palindromic_substring(A, 0, len(A)-1)


if __name__ == '__main__':
    a = "abfgba"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')