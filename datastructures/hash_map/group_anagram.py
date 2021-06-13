class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def sort_string(self, string):
        ascii_start = 97
        freq_array = [0] * 26
        for char in string:
            index = ord(char) - ascii_start
            freq_array[index] += 1
        sorted_string = ""
        for j in range(len(freq_array)):
            if freq_array[j]:
                ascii_value = ascii_start + j
                for k in range(freq_array[j]):
                    sorted_string += chr(ascii_value)
        print(sorted_string)
        return sorted_string

    def anagrams(self, A):
        string_hash_map = dict()
        ans = list()

        for i in range(len(A)):
            sorted_string = self.sort_string(A[i])
            if sorted_string not in string_hash_map:
                string_hash_map[sorted_string] = list()
                string_hash_map[sorted_string].append(i+1)
            else:
                string_hash_map[sorted_string].append(i+1)

        for string in string_hash_map.keys():
            ans.append(string_hash_map[string])
        
        return ans


if __name__ == "__main__":
    a = ['rat', 'tar', 'art']
    obj = Solution()
    ans = obj.anagrams(a)
    print(ans)
