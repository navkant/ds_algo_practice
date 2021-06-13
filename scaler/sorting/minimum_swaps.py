class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        count = 0

        for i in range(n):
            A[i] = (i, A[i])

        visit_array = [False] * n
        A = sorted(A, key=lambda x: x[1])
        print(visit_array)
        print(A)
        print()
        count = 0
        for i in range(n):
            j = i
            cycle_size = 0
            while not visit_array[j]:
                visit_array[j] = True
                j = A[j][0]
                cycle_size += 1
                print(visit_array)

            if cycle_size:
                count += cycle_size - 1

        return count


if __name__ == '__main__':
    a = [1, 3, 4, 0, 2]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')