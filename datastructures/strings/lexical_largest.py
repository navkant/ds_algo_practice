class Solution:
    # @param A : string
    # @return a strings
    def getLargest(self, A):
        original_string = A.split('_')[0]
        replacement_string = A.split('_')[1]
        replacement_string = ''.join(sorted(replacement_string)[::-1])
        print(replacement_string)
        hash_map = dict()

        for i in replacement_string:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        output_string = ''
        for i in range(len(original_string)):
            char_found = False
            max_index = 0

            for j in range(len(replacement_string)):
                # print(hash_map[replacement_string[j]])
                if (hash_map[replacement_string[j]] > 0) and (ord(replacement_string[j]) > ord(original_string[i])):
                    max_index = j
                    break
            # print()
            if ord(original_string[i]) < ord(replacement_string[max_index]) and hash_map[replacement_string[max_index]] > 0:
                # print("YESSSS: ", replacement_string[max_index])
                output_string = output_string + replacement_string[max_index]
                hash_map[replacement_string[max_index]] -= 1
                char_found = True
            else:
                pass
            
            if not char_found:
                # print('NOOO')
                output_string = output_string + original_string[i]
            else:
                pass
        return output_string


if __name__ == "__main__":
    a = 'ittmcsvmoa_jktvvblefw'
    print(a)
    obj = Solution()
    ans = obj.getLargest(a)
    print('ans is: ', ans)