class Solution:
    # @param A : string
    # @return an integer

    def lps(self, string):
        print(string)
        if len(string) == 1 or len(string) == 0:
            return len(string)

        if string[0] == string[-1]:
            return 2 + self.lps(string[1:-1])

        else:
            return max(self.lps(string[:-1]), self.lps(string[1:]))

    def solve(self, A):
        return self.lps(A)


if __name__ == '__main__':
    a = "bebdeeedaddecebbbbbabebedc"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')