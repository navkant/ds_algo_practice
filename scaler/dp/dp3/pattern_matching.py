class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def is_match_recurse(self, str1, str2, m, n):
        print(f'm: {m} n {n}')
        if str2 == '*':
            return 1

        if n < 0 or m < 0:
            if n < 0 and m < 0:
                return 1

            if n < 0:
                return 0

            if m < 0:
                if str2[n] == '*' and self.is_match_recurse(str1, str2, m, n-1):
                    return 1
                else:
                    return 0

        if str2[n] == '?':
            return self.is_match_recurse(str1, str2, m-1, n-1)
        if str2[n] == '*':
            return self.is_match_recurse(str1, str2, m - 1, n)
            # return self.is_match_recurse(str1, str2, m, n-1) or self.is_match_recurse(str1, str2, m-1, n)
        if str1[m] == str2[n]:
            return 1 and self.is_match_recurse(str1, str2, m-1, n-1)
        else:
            return 0

    def isMatch(self, A, B):
        x = len(A)
        y = len(B)
        return self.is_match_recurse(A, B, x-1, y-1)


if __name__ == '__main__':
    a = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    b = 'a*'
    obj = Solution()
    ans = obj.isMatch(a, b)
    print(f'ans is {ans}')
