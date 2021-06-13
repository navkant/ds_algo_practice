class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        y = len(A)
        x = len(A[0])

        j = 0
        for i in range(1, x):
            A[j][i] = A[j][i-1] + A[j][i]

        j = 0
        for i in range(1, y):
            A[i][j] = A[i-1][j] + A[i][j]

        for i in range(1, y):
            for j in range(1, x):
                A[i][j] = min(A[i-1][j] + A[i][j], A[i][j-1] + A[i][j])

        return A[-1][-1]


if __name__ == '__main__':
    a = [[1, 3, 2],
         [4, 3, 1],
         [5, 6, 1]]

    obj = Solution()
    ans = obj.minPathSum(a)
    print(f'ans is {ans}')
