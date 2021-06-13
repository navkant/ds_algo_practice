class Solution:
    def __init__(self):
        self.ath_term = 0

    def ath_fibonacci_recursive(self, first, second, A, postion):
        if A <= 1:
            self.ath_term = A
            return

        if postion == A:
            self.ath_term = second
            return

        self.ath_fibonacci_recursive(second, second+first, A, postion+1)

    def ath_fibonaccu_iterative(self, A):
        if A <= 1:
            return A

        first = 0
        second = 1
        for i in range(2, A+1):
            temp = first
            first = second
            second = temp + second
        return second

    def solve(self, A):
        f = 0
        s = 1
        self.ath_fibonacci_recursive(f, s, A, 1)
        print(f'recursive ans is {self.ath_term}')

        ans = self.ath_fibonaccu_iterative(A)
        print(f'iterative ans is {ans}')



if __name__ == '__main__':
    a = 6
    obj = Solution()
    obj.solve(a)
