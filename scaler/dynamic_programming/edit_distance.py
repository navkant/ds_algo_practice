class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        n = len(A)
        m = len(B)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0:
                    dp[i][j] = j
                if j == 0:
                    dp[i][j] = i

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


if __name__ == '__main__':
    a = "b"
    b = "a"

    obj = Solution()
    ans = obj.minDistance(a, b)
    print(f'ans is {ans}')
