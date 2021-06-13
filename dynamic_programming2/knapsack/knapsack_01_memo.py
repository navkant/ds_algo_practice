class Solution:
    def __init__(self, n, cap):
        self.t = []
        for i in range(n+1):
            row = []
            for j in range(cap+1):
                row.append(-1)
            self.t.append(row)

    def print_dp_matrix(self):
        for x in self.t:
            print(x)

    def knapsack(self, wt_array, val_array, cap, n):
        if cap == 0 or n == 0:
            return 0
        if self.t[n][cap] != -1:
            return self.t[n][cap]

        if wt_array[n-1] <= cap:
            value = max(val_array[n-1] + self.knapsack(wt_array, val_array, cap - wt_array[n-1], n-1), self.knapsack(wt_array, val_array, cap, n-1))
            self.t[n][cap] = value
            return value
        else:
            value = self.knapsack(wt_array, val_array, cap, n-1)
            return value


if __name__ == "__main__":
    weight_array = [1, 3, 4, 5]
    value_array = [2, 4, 5, 7]
    capacity = 7
    sol_obj = Solution(len(weight_array), capacity)
    profit = sol_obj.knapsack(weight_array, value_array, capacity, len(weight_array))
    print(profit)
