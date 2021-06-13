class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = dict()

        for i in range(len(A)-1, -1, -1):
            if A[i] not in hash_map:
                hash_map[A[i]] = i
            else:
                pass
        print(hash_map)

        min_index = 10 ** 7
        for k in hash_map.keys():
            min_index = min(min_index, hash_map[k])

        return A[min_index]


if __name__ == '__main__':
    a = [1, 2, 3, 2, 3, 2, 3, 1]
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is : ', ans)
