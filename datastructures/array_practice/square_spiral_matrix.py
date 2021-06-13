class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0 for i in range(A)] for j in range(A)]
        for i in matrix:
            print(i)

        left = 0
        right = A - 1
        top = 0
        bottom = A - 1
        count = 1
        while (left <= right) and (top <= bottom):
            for i in range(left, right+1):
                matrix[top][i] = count
                count += 1
            top += 1

            for i in range(top, bottom+1):
                matrix[i][right] = count
                count += 1
            right -= 1

            for i in range(right, left-1, -1):
                matrix[bottom][i] = count
                count += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                matrix[i][left] = count
                count += 1
            left += 1




if __name__ == "__main__":
    A = 3
    obj = Solution()
    obj.generateMatrix(A)