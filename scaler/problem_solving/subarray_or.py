class Solution:
    def cnt(self, n):
        return (n * (n+1))//2

    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(32):
            C = self.cnt(n)
            c = 0
            for j in range(n):
                if (A[j] >> i) & 1:
                    C -= self.cnt(c)
                    c = 0
                else:
                    c += 1
            C -= self.cnt(c)

            ans = ans + (C * (1 << i))
        return ans


if __name__ == '__main__':
    a = [7, 8, 9, 10]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
