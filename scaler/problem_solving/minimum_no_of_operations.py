class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hash_map = dict()

        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] not in hash_map:
                    hash_map[A[i][j]] = 1
                else:
                    hash_map[A[i][j]] += 1

        keys = list(hash_map.keys())
        minn = keys[0]
        maxx = keys[0]

        for i in range(1, len(keys)):
            if (keys[i] - keys[i-1]) % B != 0:
                return -1
            else:
                pass

            minn = min(minn, keys[i])
            maxx = max(maxx, keys[i])

        print(minn)
        print(maxx)
        return 1


if __name__ == '__main__':
    A = [[0, 2, 8],
         [8, 2, 0],
         [0, 2, 8]]
    B = 2

    obj = Solution()
    ans = obj.solve(A, B)
    print(f'ans is {ans}')


