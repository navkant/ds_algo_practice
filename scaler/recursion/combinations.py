class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine_recursive(self, start, a, b, res, comb):
        if start > a:
            if len(comb) == b:
                res.append([i for i in comb])
            return

        if len(comb) == b:
            res.append([x for x in comb])
            return

        self.combine_recursive(start + 1, a, b, res, comb + [start])
        self.combine_recursive(start + 1, a, b, res, comb)

    def combine(self, A, B):
        ans = []
        self.combine_recursive(1, a, b, ans, [])
        print(f'ans is {ans}')


if __name__ == '__main__':
    a = 4
    b = 2
    obj = Solution()
    obj.combine(a, b)