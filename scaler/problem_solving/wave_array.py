class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()

        for i in range(0, len(A)-1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
            print(A)

        return A


if __name__ == '__main__':
    a = [5, 1, 3, 2, 4]
    # [1, 2, 3, 4, 5]
    obj = Solution()
    ans = obj.wave(a)
    print(f'ans is {ans}')
