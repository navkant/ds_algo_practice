class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        print(A)
        hash_map = {}
        i = 0
        j = 1
        count = 0
        while i < n and j < n:
            if abs(A[i] - A[j]) == B:
                if (A[i], A[j]) not in hash_map:
                    print(f'A[i] {A[i]} A[j] {A[j]}')
                    hash_map[(A[i], A[j])] = [A[i], A[j]]
                    count += 1
                else:
                    print(hash_map)
                    if i != hash_map[(A[i], A[j])][-2] and j != hash_map[(A[i], A[j])][-1]:
                        hash_map[(A[i], A[j])].extend([i, j])
                        count += 1
                    else:
                        pass
                i += 1
            elif abs(A[i] - A[j]) > B:
                i += 1
                j += 1
            elif abs(A[i] - A[j]) < B:
                j += 1

        return count


if __name__ == '__main__':
    a = [1, 8, 2, 8, 8, 8, 8, 4, 4, 6, 10, 10, 9, 2, 9, 3, 7]
    b = 1
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
