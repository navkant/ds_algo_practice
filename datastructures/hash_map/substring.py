class Solution:

    def get_substring(self, string, start, output, ans, required_length):
        if len(output) ==  required_length and output not in ans:
        # if  output not in ans:
            ans.append(output) 
        if start == len(string):
            return
        self.get_substring(string, start+1, output, ans, required_length)
        output = output + string[start]
        self.get_substring(string, start+1, output, ans, required_length)
        return ans



if __name__ == "__main__":
    a = "abcbacabc"
    obj = Solution()
    start = 0
    output = ''
    ans = list()
    x = obj.get_substring(a, 0, output, ans, 3)
    print(x)

