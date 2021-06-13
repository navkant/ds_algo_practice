class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        for i in range(len(A)):
            for j in range(1, len(A[i])):
                A[i][j] += A[i][j - 1]

        for i in range(len(A[0])):
            for j in range(1, len(A)):
                A[j][i] += A[j - 1][i]

        ans = list()
        for i in A:
            print(i)

        for i in range(len(B)):
            x1 = B[i]-1
            y1 = C[i]-1
            x2 = D[i]-1
            y2 = E[i]-1

            if x1 == 0 and y1 == 0:
                sum = A[x2][y2]
                ans.append(sum)
            elif x1 == 0 and y1 != 0:
                sum = A[x2][y2] - A[x2][y1 - 1]
                ans.append(sum)
            elif x1 != 0 and y1 == 0:
                sum = A[x2][y2] - A[x1 - 1][y2] - A[x2][y1] + A[x1 - 1][y1]
                ans.append(sum)
            else:
                sum = A[x2][y2] - A[x1 - 1][y2] - A[x2][y1 - 1] + A[x1 - 1][y1 - 1]
                ans.append(sum % ((10 ** 9) + 7))
        return ans


if __name__ == '__main__':
    a = [[5, 17, 100, 11],
         [0, 0, 2, 8]]
    B = [1, 1]
    C = [1, 4]
    D = [2, 2]
    E = [2, 4]
    obj = Solution()
    ans = obj.solve(a, B, C, D, E)
    print(f'ans is {ans}')
