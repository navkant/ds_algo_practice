import sys


class Solution:
    # @param A : list of integers
    # @return an integer

    def get_gcd(self, a, b):
        if b == 0:
            return a
        if a == 0:
            return b

        if b < a:
            return self.get_gcd(b, a % b)
        else:
            return self.get_gcd(a, b % a)

    def solve(self, A):
        n = len(A)
        pre = [0] * n
        suff = [0] * n
        pre[0] = A[0]
        suff[n-1] = A[n-1]

        print(pre)
        for i in range(1, n):
            pre[i] = self.get_gcd(pre[i-1], A[i])
        print(pre)

        for i in range(n-2, -1, -1):
            suff[i] = self.get_gcd(suff[i+1], A[i])
        print(suff)
        ans =  -1

        for i in range(n):
            if i == 0:
                ans = max(ans, suff[i+1])
            elif i == n-1:
                ans = max((ans, pre[i-1]))
            else:
                ans = max(ans, self.get_gcd(pre[i-1], suff[i+1]))

        return ans


if __name__ == '__main__':
    a = [3, 9, 6, 8, 3]
    # c = [1, 1, 1, 1, 3]
    # b = [3, 3, 3, 1, 1]

    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
