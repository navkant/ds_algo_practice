class Solution:
    # @param A : string
    # @return an integer

    def get_palindrome_dp(self, string):
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
        return dp

    def get_min_partitions(self, string):
        n = len(string)
        pal_dp = self.get_palindrome_dp(string)

        for row in pal_dp:
            print(row)

        dp = [i for i in range(n)]
        print(string)
        if string[0] == string[1]:
            dp[1] = 0

        for i in range(2, n):
            if pal_dp[0][i]:
                dp[i] = 0
                continue

            for j in range(1, i+1):
                if pal_dp[j][i]:
                    dp[i] = min(dp[i], 1 + dp[j-1])

        print(dp)

        return dp[-1]

    def minCut(self, A):
        if len(A) == 1:
            return 0

        return self.get_min_partitions(A)


if __name__ == '__main__':
    a = ""
    obj = Solution()
    ans = obj.minCut(a)
    print(f'ans is {ans}')