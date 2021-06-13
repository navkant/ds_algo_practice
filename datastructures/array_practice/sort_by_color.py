class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        hash_map = dict()
        
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        output_array = list()
        keys = sorted(list(hash_map.keys()))
        
        for k in keys:
            for i in range(hash_map[k]):
                output_array.append(k)
        return output_array

if __name__ == "__main__":
    a = [ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0, 2, 1, 1, 0, 1, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 2, 0, 2, 0, 1, 1, 0, 2, 2, 1, 2, 0, 2, 1, 1, 1, 2, 0, 1, 0, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 2, 1, 1, 0, 2, 1, 2, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 1, 1, 0, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 0, 1, 2, 1, 1, 0, 1, 2, 0, 1, 0, 2, 2, 1, 2, 1, 0, 2, 2, 1, 1, 0, 2, 1, 2 ]
    obj = Solution()
    ans = obj.sortColors(a)
    print(ans)