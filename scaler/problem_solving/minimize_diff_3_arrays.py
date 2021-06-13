import sys


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        i = 0
        j = 0
        k = 0

        minn = sys.maxsize

        while i < len(A) and j < len(B) and k < len(C):
            elements = sorted([A[i], B[j], C[k]])
            print(elements, end=' ')
            if elements[0] == A[i]:
                i += 1
            elif elements[0] == B[j]:
                j += 1
            else:
                k += 1

            local_min = min(elements)
            local_max = max(elements)
            print(f'localmax: {local_max} localmin: {local_min}')
            diff = local_max - local_min
            minn = min(minn, diff)
            print()
        return minn


if __name__ == '__main__':
    A = [1, 4, 5, 8, 10]
    B = [6, 9, 15]
    C = [2, 3, 6, 6]

    obj = Solution()
    ans = obj.solve(A, B, C)
    print(f'ans is: {ans}')


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0

        similar_count = 1
        for i in range(1, len(A)):
            if A[i] == A[i - 1]:
                similar_count += 1
            else:
                similar_count = 1

            if similar_count > 2:
                A.remove(A[i])
                count += 1

        return len(A) - count
