class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def ismatch_recursive(self, string, pattern, i, j):
        if i < 0 or j < 0:
            if i < 0 and j < 0:
                return 1
            if j < 0:
                return 0

            if i < 0 and pattern[j] == '*':
                if self.ismatch_recursive(string, pattern, i, j-2):
                    return 1
                else:
                    return 0

        if string[i] == pattern[j] or pattern[j] == '.':
            return self.ismatch_recursive(string, pattern, i-1, j-1)
        if pattern[j] == '*':
            x1 = self.ismatch_recursive(string, pattern, i, j-2)
            x2 = False
            if string[i] == pattern[j-1]:
                x2 = self.ismatch_recursive(string, pattern, i-1, j)
            return x1 or x2
        else:
            return 0

    def isMatch(self, A, B):
        ans = self.ismatch_recursive(A, B, len(A)-1, len(B)-1)
        print(f'recursive ans is {ans}')


if __name__ == '__main__':
    a = 'abbbc'
    b = 'ab*c'
    obj = Solution()
    obj.isMatch(a, b)