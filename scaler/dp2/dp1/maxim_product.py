class Solution:
    def solve_recursive(self, arr, n):
        if n < 1:
            return arr[0]

        return max(self.solve_recursive(arr, n-1),
                   self.solve_recursive(arr, n-1) * arr[n])

    def solve_iterative(self, array):
        n = len(array)
        dp1 = [0] * n
        dp2 = [0] * n

        dp1[0] = array[0]
        dp2[0] = array[0]

        for i in range(1, n):
            maxx = max(array[i], dp1[i - 1] * array[i], dp2[i - 1] * array[i])
            minn = min(array[i], dp1[i - 1] * array[i], dp2[i - 1] * array[i])
            dp1[i] = maxx
            dp2[i] = minn

        return max(dp1)

    def solve(self, arr):
        ans = self.solve_iterative(arr)
        print(f'iterative ans is {ans}')
        n = len(arr)
        ans1 = self.solve_recursive(arr, n-1)
        print(f'recursive ans is {ans1}')


if __name__ == '__main__':
    a = [-3, 0, -5, 0]
    obj = Solution()
    ans = obj.solve(a)

