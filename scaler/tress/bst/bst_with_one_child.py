import sys

class Solution:
    # @param A : list of integers
    # @return a strings

    def solve(self, A):
        n = len(A)

        if n == 2:
            if A[1] > A[0]:
                return "YES"
            else:
                return "NO"

        minn = -1 * sys.maxsize
        maxx = sys.maxsize
        for i in range(1, n):
            if A[i] < A[i-1]:
                maxx = A[i-1]
                if minn < A[i] < maxx:
                    pass
                else:
                    return "No"
            elif A[i] > A[i-1]:
                minn = A[i-1]
                if minn < A[i] < maxx:
                    pass
                else:
                    return "No"
            else:
                return "NO"

        return "YES"


if __name__ == '__main__':
    a = [1, 5, 6, 4]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')