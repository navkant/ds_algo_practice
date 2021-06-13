class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):

        for i in range(1, len(A)):
            A[i] = A[i] + A[i - 1]
        print(A)
        ans = list()

        for q in B:
            if q[0] != 1:
                summ = A[q[1] - 1] - A[q[0] - 1]
            else:
                summ = A[q[1] - 1]
            row = [0, 0]
            zero_count = (q[1] - q[0] + 1) - summ
            row[1] = zero_count
            if summ % 2 != 0:
                row[0] = 1
            else:
                row[0] = 0
            print(f'SUM: {summ} zero_count: {zero_count}')
            ans.append(row)

        return ans


if __name__ == '__main__':
    a = [1, 0, 0, 0, 1]
    b = [
        [2, 4],
        [1, 5],
        [3, 5]]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')