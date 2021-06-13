class Solution:
    """This part of knapsack problem calculates maximum value of weights that can be carried in the bag of given
    capacity -- using bottom up approach"""

    def __init__(self, wt_array, val_array, i, j):
        self.wt_array = wt_array
        self.val_array = val_array
        self.memo = [[0 for x in range(j+1)] for y in range(i+1)]

    def knapsack_bottom_up(self, n, cap):
        for i in range(1, n+1):
            for j in range(1, cap+1):
                if self.wt_array[i-1] <= j:
                    self.memo[i][j] = max(self.val_array[i-1] + self.memo[i-1][j - self.wt_array[i-1]],
                                          self.memo[i-1][j])
                else:
                    self.memo[i][j] = self.memo[i-1][j]
        return self.memo[-1][-1]


if __name__ == '__main__':
    wt_array = [10, 20, 90]
    val_array = [60, 100, 120]
    capacity = 50
    n = len(wt_array)
    sol = Solution(wt_array, val_array, len(wt_array), capacity)
    ans = sol.knapsack_bottom_up(n, capacity)
    print(sol.memo)
    print(ans)