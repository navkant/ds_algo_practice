class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def longest_common_subsequence(self, str1, str2, m, n):
        if m == -1 or n == -1:
            return 0

        if str1[m] == str2[n]:
            return 1 + self.longest_common_subsequence(str1, str2, m-1, n-1)
        else:
            return max(self.longest_common_subsequence(str1, str2, m-1, n),
                       self.longest_common_subsequence(str1, str2, m, n-1))

    def solve(self, A, B):
        M = len(A)
        N = len(B)
        return self.longest_common_subsequence(A, B, M-1, N-1)


if __name__ == '__main__':
    a = 'abbcdgf'
    b = 'bbadcgf'
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
