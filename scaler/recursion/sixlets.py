class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def rec_func(self, A, B, n, output, sum, count):
        if n == -1:
            return 0

        if len(output) == B:
            return 1

        print(f'output {output} B {B} count {count}')
        if sum + A[n-1] <= 1000:
            output1 = output.copy()
            output1.append(A[n-1])
            return self.rec_func(A, B, n-1, output1, sum + A[n-1], count) + self.rec_func(A, B, n - 1, output, sum, count)
        else:
            return self.rec_func(A, B, n-1, output, sum, count)

    def solve(self, A, B):
        n = len(A)
        output = []
        sum = 0
        count = 0
        return self.rec_func(A, B, n, output, sum, count)
        # return count


if __name__ == '__main__':
    a = [1, 2, 8]
    b = 2
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')