class Solution:
    def __init__(self):
        pass

    def check_palindrome(self, string, i, j):
        if i == j:
            return 1

        if i+1 == j:
            if string[i] == string[j]:
                return 2
            else:
                return 0

        if string[i] == string[j]:
            return max(2 + self.check_palindrome(string, i+1, j-1),
                       self.check_palindrome(string, i+1, j),
                       self.check_palindrome(string, i, j-1))
        else:
            return max(self.check_palindrome(string, i+1, j),
                       self.check_palindrome(string, i, j-1))

    def solve_recursive(self, string):
        return self.check_palindrome(string, 0, len(string)-1)


if __name__ == '__main__':
    a = 'aaaabbaa'
    obj = Solution()
    ans = obj.solve_recursive(a)
    print(f'ans is {ans}')
