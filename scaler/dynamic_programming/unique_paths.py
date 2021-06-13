class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        y = len(A)
        x = len(A[0])

        for i in A:
            print(i)
        print()

        for i in range(y):
            for j in range(x):
                if A[i][j] == 1:
                    A[i][j] = -1
                # if i == 0 and A[i][j] != -1:
                #     A[i][j] = 1
                #
                # if j == 0 and A[i][j] != -1:
                #     A[i][j] = 1

        i = 0
        for j in range(x):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                break

        j = 0
        for i in range(1, y):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                break

        for i in A:
            print(i)
        print()

        for i in range(1, y):
            for j in range(1, x):
                if A[i][j] == -1:
                    continue
                else:
                    if A[i-1][j] == -1 and A[i][j-1] == -1:
                        pass
                    elif A[i-1][j] == -1 and A[i][j-1] != -1:
                        A[i][j] = A[i][j-1]
                    elif A[i - 1][j] != -1 and A[i][j - 1] == -1:
                        A[i][j] = A[i - 1][j]
                    else:
                        A[i][j] = A[i - 1][j] + A[i][j-1]

        for i in A:
            print(i)

        if A[-1][-1] == -1:
            return 0
        return A[-1][-1]


if __name__ == '__main__':
    a = [[0, 1]]

    obj = Solution()
    ans = obj.uniquePathsWithObstacles(a)
    print(f'ans is {ans}')
