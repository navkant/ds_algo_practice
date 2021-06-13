# Minimum number of squares whose sum equals to given number n

import sys


class Solution:
    def min_sqrs_num(self, n):
        if n <= 3:
            return n
        res = n

        for i in range(1, n+1):
            temp = i * i
            if temp > n:
                break
            else:
                res = min(res, 1 + self.min_sqrs_num(n - temp))

        return res

    def min_sqrs_num_DP(self, N):
        dp = [0] * (N + 1)

        for i in range(4):
            print(i)
            dp[i] = i

        print(dp)
        for i in range(4, N+1):
            dp[i] = i

            for j in range(1, i+1):
                temp = j * j
                if temp > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i-temp])

        print(dp)
        return dp[N-1]


if __name__ == '__main__':
    N = 12
    obj = Solution()
    ans = obj.min_sqrs_num_DP(N)
    print(f'ans is {ans}')
