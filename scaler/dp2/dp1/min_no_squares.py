class Solution:
    def __init__(self):
        self.min_count = 9999999999999999

    def min_no_squares_recursive(self, num, summ, count):
        if summ == 0:
            self.min_count = min(self.min_count, count)

        for i in range(1, num):
            temp = i * i
            if temp <= summ:
                self.min_no_squares_recursive(num, summ-temp, count+1)
            else:
                break

    def min_no_squares_itertive(self, num):
        dp = [1] * (num + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, num+1):
            dp[i] = i
            j = 1

            while j * j <= i:
                temp = j * j
                dp[i] = min(dp[i], dp[i - temp] + 1)
                j += 1

        return dp[-1]


    def solve(self, A):
        self.min_no_squares_recursive(A, A, 0)
        print(f'recursive ans is {self.min_count}')

        ans = self.min_no_squares_itertive(A)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = 12
    obj = Solution()
    obj.solve(a)
