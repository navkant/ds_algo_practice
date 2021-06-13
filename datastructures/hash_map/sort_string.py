class Solution:

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


if __name__ == "__main__":
    s = "navkant"
    obj = Solution()
    ans = obj.sort_string(s)
    print("sorted string is: ", ans)
