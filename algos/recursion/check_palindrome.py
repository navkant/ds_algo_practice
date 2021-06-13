class Solution:
    # @param A : string
    # @return an integer
    def check_palindrome(self, string, start, end):
        if start == end:
            return True
        elif end - start == 1 and string[start] == string[end]:
            return True
        elif end - start == 1 and string[start] != string[end]:
            return False

        if string[start] == string[end]:
            return self.check_palindrome(string, start+1, end-1) and (string[start] == string[end])
        else:
            return False

    def solve(self, A):
        ans = self.check_palindrome(A, 0, len(A)-1)
        if ans:
            return 1
        else:
            return 0


if __name__ == '__main__':
    a = 'nanman'
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
