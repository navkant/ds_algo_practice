class Solution:
    def __init__(self):
        pass

    def coin_sum_dp(self, coin_arr, summ):
        n = len(coin_arr)
        dp = [[0 for j in range(summ+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, summ+1):
                if coin_arr[i-1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coin_arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        for row in dp:
            print(row)
        return dp[-1][-1]

    def coin_sum_recursive(self, arr,  n, summ, elements):
        if n < 0:
            if summ == 0:
                print(f'    n: {n} summ: {summ}  elements: {elements}')
                return 1
            else:
                print('returning 0.. n < 0')
                return 0

        if summ <= 0:
            if summ == 0:
                print(f'    n: {n} summ: {summ}  elements: {elements}')
                return 1
            else:
                print('returning 0.. summ < 0')
                return 0

        print(f'n: {n} summ: {summ}  elements: {elements}')
        elements2 = elements.copy()
        elements2.append(arr[n])

        return self.coin_sum_recursive(arr, n, summ - arr[n], elements2) + self.coin_sum_recursive(arr, n-1, summ, elements)

    def solve(self, arr, B):
        ans = self.coin_sum_recursive(arr, len(arr)-1, B, [])
        print(f'recursive ans is {ans}')


if __name__ == '__main__':
    a = [1, 3, 4]
    b = 5
    obj = Solution()
    obj.solve(a, b)
