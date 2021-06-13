class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor_value = 0
        n = len(A)

        for i in range(n):
            xor_value = xor_value ^ A[i]

        print(xor_value)

        for j in range(32):
            if (xor_value >> j) & 1:
                break

        a1 = []
        b1 = []
        for i in range(n):
            if (A[i] >> j) & 1:
                a1.append(A[i])
            else:
                b1.append(A[i])

        value1 = 0
        for i in range(len(a1)):
            value1 = value1 ^ a1[i]

        value2 = 0
        for i in range(len(b1)):
            value2 = value2 ^ b1[i]

        return [value1, value2]


if __name__ == '__main__':
    a = [ 186, 256, 102, 377, 186, 377 ]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')