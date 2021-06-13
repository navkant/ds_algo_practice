class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def __init__(self):
        self.count = 0

    def num_distinct_recursive(self, A, B, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if i < 0:
                return 0
            else:
                return 1

        if A[i] == B[j]:
            return self.num_distinct_recursive(A, B, i-1, j-1) + self.num_distinct_recursive(A, B, i-1, j)
        else:
            return self.num_distinct_recursive(A, B, i - 1, j)

    def num_distinct_dp(self, string1, string2):
        n = len(string1)
        m = len(string2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for row in dp:
            print(row)
        print()

        for i in range(1, n+1):
            for j in range(1, m+1):
                if string1[i-1] == string2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        print(f'   ""', end=' ')
        for i in range(m):
            print(f'{string2[i]} ', end=' ')
        print()
        for i, row in enumerate(dp):
            if i == 0:
                print(f'""{row}')
            else:
                print(f'{string1[i-1]} {row}')

        return dp[-1][-1]

    def numDistinct(self, A, B):
        ans = self.num_distinct_dp(A, B)
        print(f'iterative ans is {ans}')
        n = len(A)
        ans2 = self.num_distinct_recursive(A, B, len(A)-1, len(B)-1)
        print(f'recursive ans is {ans2}')


if __name__ == '__main__':
    a = 'rabbaa'
    b = 'raba'
    obj = Solution()
    obj.numDistinct(a, b)
