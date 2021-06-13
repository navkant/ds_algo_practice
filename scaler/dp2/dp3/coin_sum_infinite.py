class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.count = 0

    def coin_sum(self, coins, summ, i):
        if summ == 0:
            return 1

        if i < 0:
            if summ == 0:
                return 1
            else:
                return 0

        if coins[i] <= summ:
            return self.coin_sum(coins, summ - coins[i], i) + self.coin_sum(coins, summ, i-1)

        return self.coin_sum(coins, summ, i - 1)


    def coinchange2(self, A, B):
        n = len(A)
        ans1 = self.coin_sum(A, b, n-1)
        print(f'recursive ans is {ans1}')


if __name__ == '__main__':
    a = [1, 2, 3]
    b = 4
    obj = Solution()
    ans = obj.coinchange2(a, b)
    print(f'ans is {ans}')
    print(f'{obj.count}')
