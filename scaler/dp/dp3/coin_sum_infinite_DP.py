class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.count = 0

    def coin_sum_DP(self, coins, summ):
        n = len(coins)
        dp = [[0 for i in range(summ+1)] for j in range(n+1)]

        j = 0
        for i in range(n+1):
            dp[i][j] = 1

        for row in dp:
            print(row)
        print()

        for i in range(1, n+1):
            for j in range(1, summ+1):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        for row in dp:
            print(row)

        return dp[-1][-1]

    def coinchange2(self, A, B):
        return self.coin_sum_DP(A, B)


if __name__ == '__main__':
    a = [4, 1, 2]
    b = 5
    obj = Solution()
    ans = obj.coinchange2(a, b)
    print(f'ans is {ans}')
