class Solution:
    # @param A : string
    # @return an integer
    def get_pal_dp(self, string):
        n = len(string)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        for row in dp:
            print(row)
        print()

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue

                elif i + 1 == j:
                    if string[i] ==  string[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False

                elif string[i] == string[j]:
                    dp[i][j] = dp[i+1][j-1]

        for row in dp:
            print(row)
        
        return dp

    def min_cut_palindrome(self, string):
        n = len(string)
        pal_dp = self.get_pal_dp(string)

        dp = [i for i in range(n)]

        if string[0] == string[1]:
            dp[1] = 0
        
        for i in range(2, n):
            if pal_dp[0][i]:
                dp[i] = 0
                continue

            for j in range(i+1):
                if pal_dp[j][i]:
                    dp[i] = min(dp[i], dp[j-1] + 1)
        print(dp)
        return dp[-1]

    def minCut(self, A):
        ans = self.min_cut_palindrome(A)
        print(f'itertive ans is {ans}')


if __name__ == '__main__':
    a = 'bananas'
    obj = Solution()
    obj.minCut(a)