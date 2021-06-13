class Solution:
    # @param A : integer: number of digits
    # @param B : integer: sum of digits
    # @return an integer

    def __init__(self):
        self.count = 0

    def check(self, A, B, summ, digits_used):
        if digits_used == A:
            if summ == B:
                self.count += 1
            return

        if digits_used == 0:
            for i in range(1, 10):
                self.check(A, B, summ + i, digits_used + 1)
        else:
            for i in range(10):
                self.check(A, B, summ + i, digits_used + 1)

    def check_memogized(self, A, B, summ, digits_used, dp):
        # print(f'summ: {summ} digits used: {digits_used}')
        if digits_used == A:
            if summ == B:
                return 1
            return 0

        if summ > B:
            return 0

        if dp[summ][digits_used] != -1:
            return dp[summ][digits_used]

        if digits_used == 0:
            ans2 = 0
            for i in range(1, 10):
                ans2 += self.check_memogized(A, B, summ + i, digits_used + 1, dp)
        else:
            ans2 = 0
            for i in range(10):
                ans2 += self.check_memogized(A, B, summ + i, digits_used + 1, dp)

        dp[summ][digits_used] = ans2
        return dp[summ][digits_used]


    def solve(self, A, B):
        dp = [[-1 for i in range(A+1)] for j in range(B+1)]
        ans = self.check_memogized(A, B, 0, 0, dp)
        ans %= 1000000007
        for row in dp:
            print(row)
        print(f'memogized ans is {ans}')
        # self.check(A, B, 0, 0)
        # return self.count % 1000000007


if __name__ == '__main__':
    a = 5
    b = 18
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
