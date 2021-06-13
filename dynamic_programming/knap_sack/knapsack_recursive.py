class Solution:
    """This part of knapsack problem calculates maximum value of weigths that can be carriend in the bag of given
    capacity -- using memoization"""

    def __init__(self):
        self.memo = {}

    def knapsack_recursive(self, wt: list, val: list, cap: int, n: int):
        print(n)
        if n == 0 or cap == 0:
            return 0
        if wt[n-1] <= cap:
            return max(val[n-1] + self.knapsack_recursive(wt, val, cap - wt[n-1], n-1),
                       self.knapsack_recursive(wt, val, cap, n-1))
        else:
            return self.knapsack_recursive(wt, val, cap, n-1)


if __name__ == '__main__':
    wt_arrray = [10, 20, 90]
    val_array = [60, 100, 120]
    capacity = 50
    n = len(wt_arrray)
    sol = Solution()
    ans = sol.knapsack_recursive(wt_arrray, val_array, capacity, n)
    print(ans)
