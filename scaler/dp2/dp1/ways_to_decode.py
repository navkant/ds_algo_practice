class Solution:

    def ways_to_decode(self, string):
        if string == '0' or string == '':
            return 0
        n = len(string)
        dp = [0] * n

        if string[0] != '0':
            dp[0] = 1

        for i in range(1, n):

            if 1 <= int(string[i]) <= 9:
                dp[i] += dp[i-1]

            if int(string[i-1]) == 1:
                dp[i] += dp[i-2]

            if int(string[i-1]) == 2 and 0 <= int(string[i]) <= 6:
                dp[i] += dp[i-2]

            print(dp)

        print('  ', dp)
        return dp[-1]

    def numDecodings(self, A):
        n = len(A)
        if A == "0" or A == "":
            return 0
        dp = [0] * (n + 1)
        dp[0] = 1

        if A[0] != '0':
            dp[1] = 1

        for i in range(2, n+1):

            if 1 <= int(A[i-1]) <= 9:
                dp[i] = dp[i - 1]

            if int(A[i - 2]) == 1:
                dp[i] += dp[i - 2]

            if int(A[i - 2]) == 2 and 0 <= (int(A[i - 1])) <= 6:
                dp[i] += dp[i - 2]

            print(dp)

        print(dp)
        return dp[n] % (10**9 + 7)

    def solve(self, s):
        print(s)
        ans1 = self.ways_to_decode(s)
        print(f'my ans is {ans1}')

        ans = self.numDecodings(s)
        print(f'ans is {ans}')


if __name__ == '__main__':
    a = "10"  # 5971756562"
    obj = Solution()
    obj.solve(a)