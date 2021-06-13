class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @return an integer
    def solve(self, A, B, C, D):
        n = len(A)
        pre_max = [0] * n
        pre_max[0] = A[0] * B

        for i in range(1, n):
            maxx = max(pre_max[i-1], A[i] * B)
            pre_max[i] = maxx
        print(pre_max)

        pre_max[0] = max(pre_max[0], pre_max[0] + A[0] * C)
        for j in range(1, n):
            maxx = max(pre_max[j-1], pre_max[j] + A[j] * C)
            pre_max[j] = maxx
        print(pre_max)

        pre_max[0] = max(pre_max[0], pre_max[0] + A[0] * D)
        for k in range(1, n):
            maxx = max(pre_max[k - 1], pre_max[k] + A[k] * D)
            pre_max[k] = maxx
        print(pre_max)
        return max(pre_max)

class Solution2:

    def solve(self, A, B, C, D):
        i = -1
        ans1 = []
        for x in range(len(A)):
            ans1.append(A[x] * B)
        print(ans1)
        maxx1 = max(ans1)
        i = ans1.index(maxx1)

        j = -1
        ans2 = []
        for x in range(len(A)):
            if x < i:
                ans2.append(ans1[x])
                continue
            ans2.append(max(ans1[x], ans1[x-1] + A[x] * C))
        print(ans2)
        maxx2 = max(ans2)
        j = ans2.index(maxx2)

        k = -1
        ans3 = []
        for x in range(len(A)):
            if x < j:
                ans3.append(ans2[x])
                continue

            ans3.append(max(ans2[x], ans2[x-1] + A[x] * D))
        print(ans3)
        maxx3 = max(ans3)
        k = ans3.index(maxx3)

        print(i, j, k)


if __name__ == '__main__':
    x = [3, 2, 1]
    B = 1
    C = -10
    D = 3
    obj = Solution2()
    ans = obj.solve(x, B, C, D)
    print(f'ans is {ans}')
