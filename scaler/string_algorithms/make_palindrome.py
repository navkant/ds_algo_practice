class Solution:
    # @param A : string
    # @return an integer
    def check_palindrome(self, string):
        n = len(string)
        mid = n // 2

        for i in range(mid):
            if string[i] != string[n - 1 - i]:
                return False
            else:
                pass

        return True

    def solve(self, A):
        if self.check_palindrome(A):
            return 0

        else:
            n = len(A)
            for i in range(n):
                if self.check_palindrome(A[:n-i-1]):
                    return i + 1

            if n % 2 != 0:
                return n - 1
            else:
                return n


if __name__ == '__main__':
    a = 'babc'
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
