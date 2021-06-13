class Solution:
    # @param A : string
    # @return an integer

    def check_palindromic_substring(self, string, i, j):
        if i == j:
            return True

        if i+1 == j and string[i] == string[j]:
            return True

        if string[i] == string[j]:
            return self.check_palindromic_substring(string, i+1, j-1)
        else:
            return False

    def solve(self, A):
        return self.check_palindromic_substring(A, 0, len(A)-1)


if __name__ == '__main__':
    a = "abba"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')