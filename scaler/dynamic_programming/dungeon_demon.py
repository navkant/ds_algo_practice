import sys

class Solution:
    # @param A : list of list of integers
    # @return an integer

    def calculateMinimumHP(self, A):
        y = len(A)
        x = len(A[0])

        hp = [[sys.maxsize for i in range(x+1)] for j in range(y+1)]
        hp[x][y-1] = 1
        hp[x-1][y] = 1
        for i in hp:
            print(i)
        print()

        for i in range(x-1, -1, -1):
            for j in range(y-1, -1, -1):
                need = min(hp[i+1][j], hp[i][j+1]) - A[i][j]
                hp[i][j] = max(1, need)

        for i in hp:
            print(i)

        return hp[0][0]


if __name__ == '__main__':
    a = [[-2, -3, 3],
         [-5, -10, 1],
         [10, 30, -5]]
    obj = Solution()
    ans = obj.calculateMinimumHP(a)
    print(f'ans is {ans}')
