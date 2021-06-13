class Solution:
    # @param A : integer
    # @return a list of integers

    def getRow(self, A):
        triangle = [[1]]

        for i in range(1, A + 1):
            new_row = list()
            for j in range(i + 1):
                if j == 0:
                    new_row.append(triangle[i - 1][-1])
                elif j == i:
                    new_row.append(triangle[i - 1][-1])
                else:
                    sum = triangle[i - 1][j] + triangle[i - 1][j - 1]
                    new_row.append(sum)
            triangle.append(new_row)
        return triangle[-1]


if __name__ == '__main__':
    a = 3
    obj = Solution()
    ans = obj.getRow(a)
    print(f'ans is {ans}')