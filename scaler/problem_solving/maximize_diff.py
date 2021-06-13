import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def get_subsets_recursive(self, array, n, input, output):
        if n == 0:
            if input not in output:
                output.append(input)
            return

        self.get_subsets_recursive(array, n-1, input, output)
        input1 = input.copy()
        input1.append(array[n-1])
        self.get_subsets_recursive(array, n - 1, input1, output)

    def get_subsets(self, array, size):
        output = []
        self.get_subsets_recursive(array, len(array), [], output)
        ans = []
        for i in output:
            if len(i) == size:
                ans.append(i)
        return ans

    def solve(self, A, B):
        array_sum = 0
        for i in A:
            array_sum += i

        subsets = self.get_subsets(A, B)

        ans = sys.maxsize * -1
        for i in subsets:
            s1 = sum(i)
            s2 = array_sum - s1
            diff = abs(s1-s2)
            ans = max(ans, diff)

        return ans


if __name__ == '__main__':
    a = [70, 21, 7, 64, 44, 79, 50, 89, 68, 23, 20, 50, 65, 64, 48, 3, 46, 87]
    obj = Solution()
    ans = obj.solve(a, 2)
    print(f'ans is: {ans}')

