class Solution:
    def __init__(self, str1, str2, len1, len2):
        self.string1 = str1
        self.string2 = str2
        self.m = len1
        self.n = len2
        self.memo = list()
        for i in range(self.m + 1):
            row = list()
            for j in range(self.n + 1):
                row.append(-1)
            self.memo.append(row)

    def solve(self):
        self.lcs_substring(self.m, self.n, 0)

        max_lcs = -1
        for i in self.memo:
            for j in i:
                max_lcs = max(max_lcs, j)
        return max_lcs

    def lcs_substring(self, x, y, count):
        if x == 0 or y == 0:
            self.memo[x][y] = count
            return count

        if self.string1[x-1] == self.string2[y-1]:
            count = self.lcs_substring(x-1, y-1, count+1)

        value = max(count, max(self.lcs_substring(x-1, y, 0), self.lcs_substring(x, y-1, 0)))
        self.memo[x][y] = value
        return value


if __name__ == '__main__':
    a1 = 'abcd'
    a2 = 'abe'
    obj = Solution(a1, a2, len(a1), len(a2))
    ans = obj.solve()
    print(ans)
