class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    # def repeating_subsequence(self, string1, string2, m, n):
    #     if n == -1 or m == -1:
    #         return 0
    #
    #     if string1[m] == string2[n] and m != n:
    #         return 1 + self.repeating_subsequence(string1, string2, m-1, n-1)
    #
    #     else:
    #         return max(self.repeating_subsequence(string1, string2, m, n-1),
    #                    self.repeating_subsequence(string1, string2, m-1, n))

    def solve(self, A, B):
        # ans = self.repeating_subsequence(A, B, len(A)-1, len(B)-1)
        ans = self.repeating_subsequence(A)
        if ans >= 2:
            return 1
        else:
            return 0

    def repeating_subsequence(self, string):
        n = len(string)
        dp = [[0 for i in range(n+1)] for j in range(n+1)]


        for i in range(1, n+1):
            for j in range(1, n+1):
                if string[i-1] == string[j-1] and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        for i in dp:
            print(i)

        if dp[-1][-1] >= 2:
            return dp[-1][-1]
        else:
            return 0


if __name__ == '__main__':
    a = 'abba'
    b = 'abba'

    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
