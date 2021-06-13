class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B):
        hash_map = dict()

        for i in A:
            dis = i[0] ** 2 + i[1] ** 2
            if dis not in hash_map:
                hash_map[dis] = [i]
            else:
                hash_map[dis].append(i)

        sorted_dist = sorted(list(hash_map.keys()))
        ans = []

        for dist in sorted_dist:
            if len(hash_map[dist]) == 1:
                ans.append(hash_map[dist][0])
            else:
                ans.extend(hash_map[dist])

        return ans


if __name__ == '__main__':
    a = [[50, 35], [6, 4], [1, 26], [35, 30], [21, 14], [16, 11], [50, 35], [22, 37], [26, 3], [96, 74], [78, 63], [82, 106], [91, 107], [62, 107], [85, 82],  [74, 69],  [66, 105],  [109, 73], [76, 108],
         [63, 64], [81, 104],  [91, 106],  [68, 60],  [69, 65], [86, 67]]
    obj = Solution()
    ans = obj.solve(a, 9)
    print(f'ans is {ans}')
