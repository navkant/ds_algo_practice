import sys

class Solution:
    # @param A : list of list of integers
    # @return an integer

    def calculateMinimumHP(self, A):
        m = len(A)
        n = len(A[0])

        dp = [[sys.maxsize for i in range(n+1)] for j in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(dp[i+1][j], dp[i][j+1]) - A[i][j]
                dp[i][j] = max(1, need)

        for row in A:
            print(row)

        return dp[0][0]


if __name__ == '__main__':
    a = [[-2, -3, 3],
             [-5, -10, 1],
             [10, 30, -5]]
    obj = Solution()
    ans = obj.calculateMinimumHP(a)
    print(f'ans is {ans}')
