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


if __name__ == '__main__':
    N = 12
    obj = Solution()
    ans = obj.min_sqrs_num(N)
    print(f'ans is {ans}')
