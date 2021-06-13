class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        n = len(A)
        dp = [0] * n
        dp[0] = 1
        # dp[1] = 1
        print(dp)
        print()

        for i in range(1, n):
            dp[i] = 1

            for j in range(i):
                if A[j] < A[i] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
            print(dp)

        return max(dp)


if __name__ == '__main__':
    a = [0, 8, 4, 12, 2, 10] #  6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    obj = Solution()
    ans = obj.lis(a)
    print(f'ans is {ans}')
