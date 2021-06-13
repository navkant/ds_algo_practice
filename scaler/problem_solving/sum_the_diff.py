class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        A.sort()
        total_contribution = 0

        for i in range(n):
            if i == 0:
                no_lesser_elements = 0
            else:
                no_lesser_elements = i

            if i == n - 1:
                no_greater_element = 0
            else:
                no_greater_element = n - i - 1

            min_contribution = A[i] * (2 ** (no_greater_element))
            max_contibution = A[i] * (2 ** (no_lesser_elements))
            contribution = max_contibution - min_contribution
            total_contribution += contribution

        return total_contribution


if __name__ == '__main__':
    a = [5]
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
