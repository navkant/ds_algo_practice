class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.count = 0

    def check(self, digits, summ, B, dp):
        if digits <= 0:
            if summ == B:
                return 1
            return 0

        if summ > B:
            return 0

        if dp[digits][summ] != -1:
            return dp[digits][summ]

        ans2 = 0
        for j in range(10):
            ans2 += self.check(digits-1, summ+j, B, dp)

        dp[digits][summ] = ans2
        return dp[digits][summ]


    def solve(self, A, B):
        dp = [[-1 for i in range(B+1)] for j in range(A+1)]
        for row in dp:
            print(row)
        print()

        ans = 0

        for i in range(1, 10):
            ans += self.check(A-1, i, B, dp)

        return ans % 1000000007


if __name__ == '__main__':
    a = 75
    b = 22
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
