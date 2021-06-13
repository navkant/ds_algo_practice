class Solution:
    """This part of knapsack problem calculates maximum value of weights that can be carried in the bag of given
    capacity -- using memoization"""

    def __init__(self, i, j):
        self.memo = [[-1 for x in range(j+1)] for y in range(i+1)]
        for x in range(j+1):
            for y in range(i+1):
                if x == 0 or y == 0:
                    self.memo[y][x] = 0

    def knapsack_recursive(self, wt: list, val: list, cap: int, n: int):
        if n == 0 or cap == 0:
            return 0

        if self.memo[n][cap] != -1:
            return self.memo[n][cap]

        if wt[n-1] <= cap:
            value = max(val[n-1] + self.knapsack_recursive(wt, val, cap - wt[n-1], n-1),
                        self.knapsack_recursive(wt, val, cap, n-1))
            self.memo[n][cap] = value
            return value
        else:
            value = self.knapsack_recursive(wt, val, cap, n-1)
            self.memo[n][cap] = value
            return value


if __name__ == '__main__':
    wt_arrray = [10, 20, 30]
    val_array = [60, 100, 120]
    capacity = 50
    n = len(wt_arrray)
    sol = Solution(len(wt_arrray), capacity)
    ans = sol.knapsack_recursive(wt_arrray, val_array, capacity, n)
    print(sol.memo)
    print(ans)
