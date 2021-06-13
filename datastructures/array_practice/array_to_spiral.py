class Solution:
    def make_spiral(self, A):
        T = 0
        B = len(A)  # - 1
        L = 0
        R = len(A[0])  # - 1
        direction = 0

        final_array = []
        while T < B and L < R:
            print('T ', T)
            print('B ', B)
            print('R ', R)
            print('L ', L)
            if direction == 0:
                print('L -> R')
                for i in range(L, R):
                    final_array.append(A[T][i])
                direction = 1
                T += 1
            elif direction == 1:
                print('down')
                for j in range(T, B):
                    final_array.append(A[j][R-1])
                direction = 2
                R -= 1
            elif direction == 2:
                print('R -> L')
                for k in range((R - 1), (L - 1), -1):
                    final_array.append(A[B-1][k])
                direction = 3
                B -= 1
            elif direction == 3:
                print('Up')
                for m in range((B - 1), (T - 1), -1):
                    final_array.append(A[m][L])
                direction = 0
                L += 1
            print(final_array)
        return final_array
