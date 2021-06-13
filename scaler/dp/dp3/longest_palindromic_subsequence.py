class Solution:
    # @param A : string
    # @return an integer

    def check_palindromic_subsequence(self, string, i, j):
        if i == j:
            return 1

        if i + 1 == j and string[i] == string[j]:
            return 2

        if string[i] == string[j]:
            return 2 + self.check_palindromic_subsequence(string, i+1, j-1)
        else:
            return max(self.check_palindromic_subsequence(string, i+1, j),
                       self.check_palindromic_subsequence(string, i, j-1))

    def solve(self, A):
        return self.check_palindromic_subsequence(A, 0, len(A)-1)


if __name__ == '__main__':
    a = "bebeeed"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')