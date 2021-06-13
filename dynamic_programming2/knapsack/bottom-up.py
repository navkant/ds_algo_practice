class Solution:
    def __init__(self, n, cap):
        self.t = []
        for i in range(n+1):
            row = []
            for j in range(cap+1):
                row.append(0)
            self.t.append(row)

    def print_dp_matrix(self):
        for x in self.t:
            print(x)

    def knapsack(self, wt_array, val_array, cap, n):
        for i in range(1, n+1):
            for j in range(1, cap+1):
                if wt_array[i-1] <= j:
                    self.t[i][j] = max(val_array[i-1] + self.t[i-1][j - wt_array[i-1]], self.t[i-1][j])
                else:
                    self.t[i][j] = self.t[i-1][j]

        return self.t[-1][-1]


if __name__ == "__main__":
    weight_array = [10, 20, 90]
    value_array = [60, 100, 120]
    capacity = 50
    sol_obj = Solution(len(weight_array), capacity)
    profit = sol_obj.knapsack(weight_array, value_array, capacity, len(weight_array))
    print(profit)
