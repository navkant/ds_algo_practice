class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer

    def solve_recurse_dp(self, value_array, weight_array, capacity):
        n = len(value_array)

        dp = [[0 for j in range(capacity+1)] for i in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, capacity+1):
                if weight_array[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], value_array[i-1] + dp[i-1][j - weight_array[i-1]])

                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

    def solve_recurse(self, value_array, weight_array, total_value, capacity, i):
        if i < 0:
            return total_value

        if weight_array[i] <= capacity:
            return max(self.solve_recurse(value_array, weight_array, total_value+value_array[i], capacity-weight_array[i], i-1),
                       self.solve_recurse(value_array, weight_array, total_value, capacity, i-1))

        return self.solve_recurse(value_array, weight_array, total_value, capacity, i-1)

    def solve(self, A, B, C):
        ans = self.solve_recurse(A, B, 0, C, len(A)-1)
        print(f'recursive ans is {ans}')
        ans = self.solve_recurse_dp(A, B, C)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    A = [6, 10, 12]
    B = [10, 20, 30]
    C = 50
    obj = Solution()
    obj.solve(A, B, C)