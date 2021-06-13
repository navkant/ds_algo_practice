class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
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
        return sorted_string

    def solve(self, A, B):
        A = self.sort_string(A)
        i = 0
        count = 0

        while True:
            if i >=  len(B):
                break

            upper_index = i + len(A)
            if upper_index >= len(B):
                upper_index = len(B)

            substring = B[i:upper_index]
            # for x in range(i, upper_index):
            #     substring = substring + B[x]

            substring = self.sort_string(substring)

            if substring == A:
                print(substring)
                count += 1
            i += 1
        return count


if __name__ == "__main__":
    A = "ABCD"
    A = A.lower()
    B = "BACDGABCDA"
    B = B.lower()
    obj = Solution()
    ans = obj.solve(A,B)
    print(ans)
