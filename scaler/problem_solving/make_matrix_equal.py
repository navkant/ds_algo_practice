class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A[0]) == 1:
            return 0
        hash_map = dict()

        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] not in hash_map:
                    hash_map[A[i][j]] = 1
                else:
                    hash_map[A[i][j]] += 1

        keys = list(hash_map.keys())

        for i in range(1, len(keys)):
            if (keys[i] - keys[i - 1]) % B != 0:
                return -1
            else:
                pass

        n = len(keys)
        ans = 0

        mid = n // 2
        for k in keys:
            ans += (abs(keys[mid] - k) // B) * hash_map[k]
            print(ans)
        return ans


if __name__ == '__main__':
    A = []
    B = []

    obj = Solution()
    ans = obj.solve(A, B)
    print(f'ans is {ans}')
