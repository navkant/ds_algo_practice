class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hash_map = {}
        
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        ans = []
        common_hashmap = {}
        for j in B:
            if j in hash_map:
                if j not in common_hashmap:
                    common_hashmap[j] = 1
                else:
                    common_hashmap[j] += 1

        ans = list()
        for k in common_hashmap.keys():
            for i in range(min(common_hashmap[k], hash_map[k])):
                ans.append(k)
        return ans

if __name__ == "__main__":
    a = [ 2, 1, 4, 10 ]
    b = [ 3, 6, 2, 10, 10 ]
    obj = Solution()
    x = obj.solve(a, b)
    print(x)