class Solution:
    def solve(self, A, B, C, D):
        n = len(A)
        pre_max = [0] * n

        pre_max[0] = A[0] * B
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], A[i] * B)

        print(pre_max)

        pre_max[0] = max(pre_max[0], pre_max[0] + A[0] * C)
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], pre_max[i] + A[i] * C)

        print(pre_max)
        pre_max[0] = max(pre_max[0], pre_max[0] + A[0] * D)
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], pre_max[i] + A[i] * D)

        print(pre_max)

        return max(pre_max)


if __name__ == '__main__':
    a = [1, 5, -3, 4, 2]
    b = 2
    c = -1
    d = -1
    print(a)
    print()
    obj = Solution()
    ans = obj.solve(a, b, c, d)
    print(f'ans is {ans}')
