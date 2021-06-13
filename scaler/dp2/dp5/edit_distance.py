class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def min_distance_recursive(self, string1, string2, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 0
            elif i < 0:
                return j+1
            else:
                return i+1

        if string1[i] == string2[j]:
            return self.min_distance_recursive(string1, string2, i-1, j-1)
        else:
            return 1 + min(self.min_distance_recursive(string1, string2, i-1, j-1),
                           self.min_distance_recursive(string1, string2, i-1, j),
                           self.min_distance_recursive(string1, string2, i, j-1))

    def min_distance_dp(self, string1, string2):
        n = len(string1)
        m = len(string2)

        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for j in range(1, n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            dp[i][0] = i

        for i in range(1, m+1):
            for j in range(1, n+1):
                if string2[i-1] == string1[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],
                                   dp[i][j-1],
                                   dp[i-1][j])

        return dp[-1][-1]


    def minDistance(self, A, B):
        ans = self.min_distance_recursive(A, B, len(A)-1, len(B)-1)
        print(f'recursive ans is {ans}')
        ans = self.min_distance_dp(A, B)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = 'abc'
    b = 'def'
    obj = Solution()
    obj.minDistance(a, b)
