class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)
        if A == "0" or A == "":
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        if A[0] != '0':
            dp[1] = 1
        print(dp)
        # if n == 2:
        #     if int(A[1]) == 0:
        #         dp[2] = dp[1]
        #     else:
        #         pass

        for i in range(2, n+1):
            if 1 <= int(A[i-1]) <= 9:
                dp[i] = dp[i - 1]
            if int(A[i - 2]) == 1:
                dp[i] += dp[i - 2]
            if int(A[i - 2]) == 2 and 0 <= (int(A[i - 1])) <= 6:
                dp[i] += dp[i - 2]
            print(dp)

        # print(dp)
        return dp[n]


if __name__ == '__main__':
    a = "0799733"
    obj = Solution()
    ans = obj.numDecodings(a)
    print(f'ans is {ans}')


"""

1 2 1
A B A

12 1
L A

1 21
A U

"""