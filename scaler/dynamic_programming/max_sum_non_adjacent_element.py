class Solution1D:
    # @param A : list of list of integers
    # @return an integer
    def find_recurse(self, A, n):
        if n == 0 or n == 1:
            if n == 1:
                return max(A[0], A[1])
            else:
                return A[0]

        return max(self.find_recurse(A, n-1), self.find_recurse(A, n-2) + A[n])

    def find_bottom_up(self, A):
        n = len(A)
        dp = [0] * n
        dp[0] = A[0]
        dp[1] = max(A[0], A[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], A[i] + dp[i-2])

        return dp[-1]

    def adjacent(self, arr):
        # return max(self.find_recurse(arr, 0, len(arr)-1, 0), self.find_recurse(arr, 0, len(arr)-1, 1))
        return self.find_recurse(arr, len(arr)-1)


class Solution2D:
    def find_recursive(self, A, m, n):
        if m <= 1 or n <= 1:
            if m == 0 and n == 0:
                return A[0][0]

            if m == 1 and n != 1:
                return max(A[1][0], A[0][0])

            if m != 1 and n == 1:
                return max(A[0][1], A[0][0])

            if n == 1 and m == 1:
                return max(A[0][0], A[0][1],
                           A[1][0], A[1][1])

        return max(self.find_recursive(A, m-1, n-1),
                   self.find_recursive(A, m-1, n),
                   self.find_recursive(A, m, n-1),
                   self.find_recursive(A, m-2, n-2) + A[m, n],
                   self.find_recursive(A, m-2, n) + A[m, n],
                   self.find_recursive(A, m, n-2) + A[m, n])

    def adjacent(self, A):
        return self.find_recursive(A, len(A)-1, len(A[0])-1)


if __name__ == '__main__':
    a = [2, 3, 5, 0, 7, 10]
    obj = Solution1D()
    ans = obj.adjacent(a)
    print(f'ans from recursice approach {ans}')
    ans = obj.find_bottom_up(a)
    print(f'ans from bottom up {ans}')

    a = [[1, 2, 3, 4],
         [2, 3, 4, 5]]
    obj = Solution2D()
    ans = obj.adjacent(a)
    print(f'ans is {ans}')