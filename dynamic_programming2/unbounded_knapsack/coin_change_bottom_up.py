class Solution:
    def __init__(self, coin_array, amount):
        self.coin_array = coin_array
        self.amount = amount
        self.t = list()

        for i in range(len(self.coin_array) + 1):
            row = list()
            for j in range(self.amount + 1):
                if i == 0 and j == 0:
                    row.append(1)
                elif i != 0 and j == 0:
                    row.append(1)
                else:
                    row.append(0)
            self.t.append(row)
        for x in self.t:
            print(x)
        print('')

    def solve(self):
        for i in range(1, len(self.coin_array) + 1):
            for j in range(1, self.amount + 1):
                if coin_array[i-1] <= j:
                    self.t[i][j] = self.t[i][j - coin_array[i-1]] + self.t[i-1][j]
                else:
                    self.t[i][j] = self.t[i-1][j]
        for i in self.t:
            print(i)
        return self.t[-1][-1]

if __name__ == '__main__':
    coin_array = [18, 24, 23, 10, 16, 19, 2, 9, 5, 12, 17, 3, 28, 29, 4, 13, 15, 8]
    amt = 458
    obj = Solution(coin_array, amt)
    ans = obj.solve()
    print(ans)
