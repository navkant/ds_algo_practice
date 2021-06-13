import sys


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def find_min(self, A, global_minn, local_minn):
        for i in range(1, len(A)):
            if A[i] == local_minn or A[i] < local_minn:
                continue
            else:
                local_minn = min(A[i], local_minn)
        return local_minn

    def kthsmallest(self, A, B):
        g_minn = sys.maxsize
        for i in range(B):
            minn = self.find_min(A, g_minn, A[0])
            print(f'{i} : {minn}')

        return minn


if __name__ == '__main__':
    a = [33, 8, 16, 80, 55, 32, 38, 40, 65, 15]
    # print(X)
    obj = Solution()
    ans = obj.kthsmallest(a, 4)
    print(f'ans is: {ans}')