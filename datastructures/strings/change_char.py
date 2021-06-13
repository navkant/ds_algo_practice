class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hash_map = {}
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        freq_array = [''] * 26

        for key in hash_map.keys():
            if hash_map[key] == '':
                freq_array[hash_map[key]] = key
            else:
                freq_array[hash_map[key]] += key
        print(freq_array)

        distinct_count = len(hash_map.keys())

        for i in range(len(freq_array)):
            if freq_array[i] != '':
                if len(freq_array[i]) == 1:
                    if i < B:
                        B -= i
                        distinct_count -= 1
                    else:
                        pass
        return distinct_count


if __name__ == "__main__":
    a = "abcabbccd"
    obj = Solution()
    ans = obj.solve(a, 0)
    print('ans is: ', ans)
