class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        count = 0
        indices = list()
        similar_count = 1
        i = 0
        n = len(A)
        while True:
            if i == len(A):
                break
            if A[i] == A[i - 1]:
                similar_count += 1
            else:
                similar_count = 1

            if similar_count > 2:
                similar_count -= 1
                indices.append(A[i])
                count += 1
            i += 1

        for index in indices:
            A.remove(index)

        return n - count


if __name__ == '__main__':
    A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
    obj = Solution()
    ans = obj.removeDuplicates(A)
    print(A)
    print(f'ans is: {ans}')