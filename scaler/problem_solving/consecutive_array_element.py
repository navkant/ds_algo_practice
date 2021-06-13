class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minn = 10 ** 7
        maxx = -1

        for i in range(len(A)):
            minn = min(A[i], minn)
            maxx = max(A[i], maxx)

        print((f'max: {maxx}  min {minn}'))
        n = len(A)

        if (maxx - minn) == n - 1:
            return 1
        else:
            return 0


if __name__ == '__main__':
    a = [ 5, 17, 100, 11 ]
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
