class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal_recurse(self, A, i, j, summ):
        if i >= len(A):
            return summ

        return min(self.minimumTotal_recurse(A, i+1, j, summ+A[i][j]),
                   self.minimumTotal_recurse(A, i+1, j+1, summ+A[i][j+1]))

    def minimumTotal_DP(self, A):
        rows = len(A) # 8

        for i in range(rows-2, -1, -1):
            for j in range(len(A[i])):
                A[i][j] = min(A[i][j] + A[i+1][j],
                              A[i][j] + A[i+1][j+1])
        return A[0][0]

    def solve(self, matrix):
        ans = self.minimumTotal_recurse(matrix, 1, 0, matrix[0][0])
        print(f'resursive solution is {ans}')




if __name__ == '__main__':
    a =   [[9],
           [3, 8],
           [0, 2, 4],
           [8, 3, 9, 0],
           [5, 2, 2, 7, 3],
           [7, 9, 0, 2, 3, 9],
           [9, 7, 0, 3, 9, 8, 6],
           [5, 7, 6, 2, 7, 0, 3, 9],]

    obj = Solution()
    ans = obj.solve(a)
