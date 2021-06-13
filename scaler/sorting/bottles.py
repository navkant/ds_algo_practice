class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self, A):
        n = len(A)
        visible_bottles = n

        hash_map = {}
        for i in A:
            if i not in hash_map:
                hash_map[i] = [1, 1]
            else:
                hash_map[i][0] += 1
                hash_map[i][1] += 1

        keys = sorted(list(hash_map.keys()))

        for i in range(len(keys) - 1):
            count = hash_map[keys[i]][0]
            j = i + 1
            while count and j < len(keys):
                if hash_map[keys[j]][1] >= count:
                    hash_map[keys[j]][1] -= count
                    visible_bottles -= count
                    count = 0
                    break
                else:
                    count -= hash_map[keys[j]][1]
                    visible_bottles -= hash_map[keys[j]][1]
                    hash_map[keys[j]][1] = 0
                    j += 1

        return visible_bottles


if __name__ == '__main__':
    a = [8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3, 8, 17, 12, 5, 3, 14, 13, 3, 2, 17, 19, 16, 8, 7, 12, 19, 10, 13, 8, 20, 16, 15, 4, 12, 3]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
