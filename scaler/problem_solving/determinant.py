class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        B = [[-87, 79, 32],
             [-93, -98, 21],
             [-87, 32, -28]]

        if len(A) == 2:
            return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
        else:
            first_term = A[0][0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1]))
            second_term = A[0][1] * ((A[1][0] * A[2][2]) - (A[1][2] * A[2][0]))
            print(A[0][2])
            print(A[1][0] * A[2][1])
            print(A[1][1] * A[2][0])
            third_term = A[0][2] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]))
            # print(first_term) # -87(2744 - 672)
            # print(second_term) # 79(2604 + 1827))
            # print(third_term) # 32(-2976 - 8526)
            return first_term - second_term + third_term


if __name__ == '__main__':
    a = [[-87, 79, 32],
            [-93, -98, 21],
            [-87, 32, -28]]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is: {ans}')
