class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        hash_map = {}

        for i in range(len(A)):
            print(hash_map)
            if B - A[i] not in hash_map:
                if A[i] not in hash_map:
                    hash_map[A[i]] = i+1
                else:
                    pass
            else:
                print(hash_map)
                return [hash_map[B - A[i]], i+1]


if __name__ == "__main__":
    a = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
    target = -3
    obj = Solution()
    a = obj.twoSum(a, target)
    print(a)