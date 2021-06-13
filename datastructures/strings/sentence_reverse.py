class Solution:
    # @param A : string
    # @return a strings

    def split_string(self, string, split_char):
        list_of_words = list()
        i = 0
        while True:
            if i >= len(string):
                break
            j = i
            word = ''

            while True:
                if j >= len(string):
                    break
                if string[j] == split_char:
                    break
                word = word + string[j]
                j += 1
            list_of_words.append(word)
            i = j + 1
        print(list_of_words)
        return list_of_words
    
    def reverse_list(self, world_list):
        n = len(world_list)
        mid = n//2

        for i in range(mid):
            start = i
            end = n - i - 1
            world_list[start], world_list[end] = world_list[end], world_list[start]

        return world_list
    
    def join_word_list(self, word_list, join_char):
        final_string = ''

        if len(word_list) == 1:
            return word_list[0]

        for i in range(len(word_list)):
            if i == 0:
                final_string += word_list[i] + ' '
            elif i == len(word_list) - 1:
                final_string += word_list[i]
            else:
                final_string += word_list[i] + join_char
        return final_string
    
    def compact_spaces(self, string):
        output_string = ""
        for char in string:
            if char != " " or ( output_string and output_string[-1] != " "):
                output_string += char
        return output_string

    def solve(self, A):
        # A = A.strip()
        # print(A)
        # A = A[::-1]
        # return ' '.join(A)
        A = A.strip()
        A = self.compact_spaces(A)
        word_list = self.split_string(A, ' ')
        reverse_word_list = self.reverse_list(word_list)
        final_ans = self.join_word_list(reverse_word_list, ' ')
        return final_ans


if __name__ == "__main__":
    a = "qxkpvo  f   w vdg t wqxy ln mbqmtwwbaegx   mskgtlenfnipsl bddjk znhksoewu zwh bd fqecoskmo"
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ' + ans + '.')
