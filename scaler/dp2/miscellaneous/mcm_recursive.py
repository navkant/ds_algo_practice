class Solution:
    def __init__(self):
        self.min_cost = float('inf')

    def mcm_recursive(self, array, i, j):
        print(f'i: {i}, j: {j}')
        if i >= j:
            print('returing')
            return 0

        min_cost = 999999999999999

        for k in range(i, j):
            left = self.mcm_recursive(array, i, k)
            right = self.mcm_recursive(array, k+1, j)
            print(f'  k: {k} i: {i} j: {j}')
            print(f'  left: {left}')
            print(f'  right: {right}')
            print(f'  current: {array[i-1] * array[k] * array[j]}')
            cost = (array[i-1] * array[k] * array[j]) + left + right
            min_cost = min(cost, min_cost)
            print(f'  min: {min_cost}')

        return min_cost

    def mcm_dp(self, array, i, j, dp):
        if i >= j:
            return 0

        min_cost = float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        for k in range(i, j):
            left = self.mcm_dp(array, i, k, dp)
            right = self.mcm_dp(array, k+1, j, dp)
            cost = (array[i-1] * array[k] * array[j]) + left + right
            min_cost = min(cost, min_cost)

        dp[i][j] = min_cost
        return min_cost

    def mc_mminimum(self, arr):
        n = len(arr)
        ans = self.mcm_recursive(arr, 1, len(arr)-1)
        print(f'recursive ans is {ans}')
        dp = [[-1 for j in range(n)] for i in range(n)]
        ans = self.mcm_dp(arr, 1, n-1, dp)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = [40, 20, 30, 10, 30]
    obj = Solution()
    obj.mc_mminimum(a)
