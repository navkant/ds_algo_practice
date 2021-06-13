class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        for i in range(32):
            if (1 << i) <= A:
                continue
            else:
                y = 1 << i
                break
        print(y)

        x = 0

        for i in range(len(bin(A)[2:])):
            if not (A >> i) & 1:
                x = x | 1 << i
            else:
                continue
        print(x)

        return x ^ y


if __name__ == '__main__':
    a = 5
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
