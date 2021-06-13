class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        summ = 0
        mod = 10**9 + 7

        for i in range(n-1):
            summ = (summ + A[i]) % mod

        for i in range(n-1-1, -1, -1):
            temp = summ - A[i]
            summ = (summ + temp) % mod

        first = A[0]
        for i in range(1, n):
            temp = A[i] % first
            summ = (summ + temp) % mod

        return summ


if __name__ == '__main__':
    a = [17, 100, 11]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
