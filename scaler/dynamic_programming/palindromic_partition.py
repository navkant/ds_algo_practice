class Solution:
    # @param A : string
    # @return an integer
    def create_pal_dp(self, string):
        n = len(string)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue
                elif j == i + 1:
                    if string[i] == string[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if string[i] == string[j] and dp[i + 1][j - 1]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
        return dp

    def minCut(self, A):
        n = len(A)
        pal_dp = self.create_pal_dp(A)
        for row in pal_dp:
            print(row)

        dp = [0] * n

        for i in range(1, n):
            if pal_dp[0][i]:
                dp[i] = 0

            for j in range(1, i+1):
                if pal_dp[j][i]:
                    dp[i] = min(dp[i], 1 + dp[j-1])
        print(dp)
        return dp[n-1]


if __name__ == '__main__':
    a = 'bananas'
    obj = Solution()
    ans = obj.minCut(a)
    print(f'ans is {ans}')