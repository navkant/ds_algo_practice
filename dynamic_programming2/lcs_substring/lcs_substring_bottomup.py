class Solution:
    def __init__(self, str1, str2, len1, len2):
        self.string1 = str1
        self.string2 = str2
        self.m = len1
        self.n = len2
        self.t = list()

        for i in range(self.m+1):
            row = list()
            for j in range(self.n+1):
                if i == 0 and j == 0:
                    row.append(0)
                elif i == 0 and j != 0:
                    row.append(0)
                elif i != 0 and j == 0:
                    row.append(0)
                else:
                    row.append(-1)
            self.t.append(row)
        for i in self.t:
            print(i)

    def solve(self):
        self.lsc_substring()
        max_lcs = -1
        for i in self.t:
            for j in i:
                max_lcs = max(max_lcs, j)

        return max_lcs

    def lsc_substring(self):
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                if self.string1[i-1] == self.string2[j-1]:
                    self.t[i][j] = self.t[i-1][j-1] + 1
                else:
                    self.t[i][j] = 0


if __name__ == '__main__':
    a1 = 'dabc'
    a2 = 'fabe'

    obj = Solution(a1, a2, len(a1), len(a2))
    ans = obj.solve()
    print(ans)
