import sys

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        m = len(B)
        l = 0
        r = m - 1

        diff = sys.maxsize
        ans = [-1, -1]
        ind = [-1, -1]

        while l < n and r >= 0:
            summ = A[l] + B[r]
            x = abs(summ - C)

            print(f'l: {l} r: {r} summ:{summ}')
            if x < diff:
                diff = x
                ans = [A[l], B[r]]
                ind = [l, r]
            elif x == diff:
                if l == ind[0]:
                    ans = [A[l], B[r]]
                    ind[1] = r

            if summ < C:
                l += 1
            else:
                r -= 1

        return ans


if __name__ == '__main__':
    a = [1]
    b = [2, 4]
    c = 4
    obj = Solution()
    ans = obj.solve(a, b, c)
    print(f'ans is {ans}')




