class Solution:
    # @param A : string
    # @return an integer

    def check_palindrome(self, string, i, j):
        if i == j:
            return 1

        if i+1 == j:
            if string[i] == string[j]:
                return 2 + self.check_palindrome(string, i+1, j)
            else:
                return self.check_palindrome(string, i+1, j)

        if string[i] == string[j]:
            return 2 + self.check_palindrome(string, i+1, j-1)
        else:
            return max(self.check_palindrome(string, i+1, j),
                       self.check_palindrome(string, i, j-1))

    def solve(self, A):
        n = len(A)
        return self.check_palindrome(A, 0, n-1)


if __name__ == '__main__':
    a = "aedsead"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')