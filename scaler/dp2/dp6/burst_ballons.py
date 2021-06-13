class Solution:
    # @param A : list of integers
    # @return an integer
    def burst_ballon_dp(self, arr):
        n = len(arr)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][i] = 1 * arr[i] * arr[i+1]
            elif i == len(arr)-1:
                dp[i][i] = arr[i-1] * arr[i] *1
            else:
                dp[i][i] = arr[i-1] * arr[i] * arr[i+1]


        for row in dp:
            print(row)
        print()
        print(arr)
        for L in range(1, n):
            for i in range(n-L):
                j = i + L
                print(f'i:{i} j:{j}')
                for k in range(i, j+1):
                    if i == 0:
                        left_coin = 1
                    else:
                        left_coin = arr[i-1]

                    if j == n-1:
                        right_coin = 1
                    else:
                        right_coin = arr[j+1]

                    if k == i:
                        left = 0
                    else:
                        left = dp[i][k-1]

                    if k == j:
                        right = 0
                    else:
                        right = dp[k+1][j]

                    print(f'  k:{k}')
                    print(f'  left_coin:{left_coin}')
                    print(f'  right_coin:{right_coin}')
                    print(f'  left:{left}')
                    print(f'  right:{right}')

                    val = left + right + (left_coin * right_coin * arr[k])
                    print(f'  val: {val}')
                    dp[i][j] = max(dp[i][j], val)

        for row in dp:
            print(row)

        return dp[0][-1]

    def solve(self, A):
        ans = self.burst_ballon_dp(A)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = [3, 1, 5, 8]
    obj = Solution()
    obj.solve(a)
