class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        i = 0
        j = 1
        hash_map = {}
        hash_map[A[0]] = 1
        count = 1

        while j < n:
            if A[j] not in hash_map:
                hash_map[A[j]] = 1
            else:
                hash_map[A[j]] += 1

            if hash_map[A[j]] > 1:
                while hash_map[A[j]] > 1:
                    hash_map[A[i]] -= 1
                    i += 1
            else:
                pass

            count += j - i + 1
            j += 1

        return count


if __name__ == '__main__':
    a = [93, 9, 12, 32, 97, 75, 32, 77, 40, 79, 61, 42, 57, 19, 64, 16, 86, 47, 41, 67, 76, 63, 24, 10, 25, 96, 1, 30, 73, 91, 70, 65, 53, 75, 5, 19, 65, 6, 96, 33, 73, 55, 4, 90, 72, 83, 54, 78, 67, 56, 8, 70, 43, 63]
    # a = [1, 1, 3, 1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')