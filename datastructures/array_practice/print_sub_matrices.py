class Solution:
    def print_sub_matrices(self, matrix):
        n = len(matrix)

        for i1 in range(n):
            for j1 in range(n):
                for i2 in range(n):
                    for j2 in range(n):
                        print(f'i1: {i1} j1: {j1} | i2: {i2} j2: {j2}')
                        i = i1
                        j = j1
                        count = 0

                        while count <= j2-j1:
                            while i <= i2:
                                while j <= j2:
                                    print(f'{matrix[i][j]}', end=',')
                                    j += 1
                                i += 1
                                j = j1
                                print()
                            count += 1

    def print_diagonally(self, matrix):
        n = len(matrix)

        for L in range(n):
            for i in range(n-L):
                j = i + L
                print(f'{matrix[i][j]}', end=' ')
            print()

    def solve(self, matrix):
        self.print_sub_matrices(matrix)
        self.print_diagonally(matrix)


if __name__ == '__main__':
    size = 4
    a = [[i*j for j in range(1, size+1)] for i in range(1, size+1)]
    print([1, 2, 3, 4],
          [2, 4, 6, 8],
          [3, 6, 9, 12],
          [4, 8, 12, 16])
    for row in a:
        print(row)
    obj = Solution()
    obj.solve(a)