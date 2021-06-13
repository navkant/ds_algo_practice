class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.count = 0

    def coin_sum(self, coins, summ, i):
        print(f'summ: {summ} i: {i} coins: {coins[i:]}')
        if summ == 0:
            print('yess')
            return 1

        if i >= len(coins):
            print('no')
            return 0

        if coins[i] <= summ:
            return self.coin_sum(coins, summ-coins[i], i) + self.coin_sum(coins, summ, i+1)

        return self.coin_sum(coins, summ, i+1)

    def coinchange2(self, A, B):
        return self.coin_sum(A, B, 0)


if __name__ == '__main__':
    a = [4, 1, 2]
    b = 5
    obj = Solution()
    ans = obj.coinchange2(a, b)
    print(f'ans is {ans}')
