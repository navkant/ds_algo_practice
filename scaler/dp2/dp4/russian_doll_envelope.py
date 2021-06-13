class Solution:
    # @param A : list of list of integers
    # @return an integer

    def count_recursive(self, array):
        array = sorted(array, key=lambda x:x[0])
        print(array)

        dp = [0] * len(array)
        dp[0] = 1

        if array[1][0] > array[0][0] and array[1][1] > array[0][1]:
            dp[1] = 1


        for i in range(2, len(array)):
            dp[i] = 1

            for j in range(i+1):
                if array[i][0] > array[j][0] and array[i][1] > array[j][1] and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]

        return dp[-1]

    def solve(self, A):
        return self.count_recursive(A)


if __name__ == '__main__':
    a = [[5, 4], [6, 4], [6, 7], [2, 3]]
    obj = Solution()
    obj.solve(a)
