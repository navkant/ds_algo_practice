class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def gcd(self, a, b):
        if b == 0:
            return a

        if a < b:
            return self.gcd(a, b % a)
        else:
            return self.gcd(b, a % b)

    def magic_below_x(self, b, c, l, x):
        # How many magical numbers are <= x?
        return int((x // b) + (x // c) - (x // l))

    def solve(self, A, B, C):
        smaller = min(B, C)
        bigger = min(B, C)

        minn = 0
        maxx = A * bigger
        print(minn, maxx)

        L = (B*C) / self.gcd(B, C)
        while minn < maxx:
            mid = minn + (maxx - minn) // 2
            print(f'min : {minn} mid {mid} max {maxx}')
            count = self.magic_below_x(B, C, L, mid)
            print(count)
            if count < A:
                minn = mid + 1
            else:
                maxx = mid

        return minn


if __name__ == '__main__':
    a = 19
    b = 11
    c = 13

    obj = Solution()
    ans = obj.solve(a, b, c)
    print(f'ans is {ans}')
