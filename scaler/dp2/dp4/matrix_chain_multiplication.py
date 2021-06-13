import sys

class Soluiton:
    def matrix_mul(self, array):
        n = len(array)-1
        dp = [[999 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for row in dp:
            print(row)

        for L in range(1, n):  # 1 -> 3
            for i in range(n-L):
                j = i + L

                print(f'i: {i} j: {j}')
                for k in range(i, j):
                    print(f'    k: {k}, product: {array[i]} * {array[j + 1]} * {array[k]}')
                    q1 = dp[i][k] + dp[k+1][j] + (array[i] * array[j+1] * array[k+1])
                    print(f'    q1: {q1}')
                    dp[i][j] = min(dp[i][j], q1)

        for row in dp:
            print(row)

        return dp[0][-1]

    def solve(self, arr):
        self.matrix_mul(array=arr)


if __name__ == '__main__':
    a = [5, 4, 6, 2, 7]
    obj = Soluiton()
    obj.solve(a)
