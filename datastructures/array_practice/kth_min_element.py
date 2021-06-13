class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        for i in range(len(A)):
            min_element = 999999999999
            for j in range(i, len(A)):
                min_element = min(min_element, A[j])
            print(f'i: {i} min_element: {min_element}')
            k = A.index(min_element)
            A[i], A[k] = A[k], A[i]
        print(A)


if __name__ == "__main__":
    a = [2, 1, 4, 3, 2]
    obj = Solution()
    ans = obj.kthsmallest(a, 3)
