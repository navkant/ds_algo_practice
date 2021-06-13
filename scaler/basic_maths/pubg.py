import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minn = sys.maxsize

        min_index = 0
        for i in range(len(A)):
            if A[i] < minn:
                min_index = i
                minn = A[i]

        new_minn = minn
        new_minn_index = min_index

        alive = len(A)
        while alive > 1:
            for i in range(len(A)):
                if i == min_index:
                    continue
                A[i] = A[i] % minn
                if A[i] == 0:
                    alive -= 1

                if A[i] < minn and A[i] != 0:
                    new_minn = A[i]
                    new_minn_index = i
                else:
                    pass

            print('new minn found', new_minn)
            minn = new_minn
            min_index = new_minn_index

        for i in A:
            if i == 0:
                continue
            minn = min(minn, i)

        print(A)
        return minn

if __name__ == '__main__':
    a = [ 4, 7 ]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
