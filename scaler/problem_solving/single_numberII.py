class Solution:
    def solve(self, A):
        n = len(A)
        ans = 0
        for i in range(32):
            count = 0
            for j in range(n):
                if (A[j] >> i) & 1:
                    count += 1
                else:
                    pass

            if (count % 3) != 0:
                ans |= 1 << i

        return ans


if __name__ == '__main__':
    a = [0, 0, 0, 1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')