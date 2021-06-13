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
                if i == 0 or j == 0:
                    row.append(0)
                else:
                    row.append(-1)
            self.t.append(row)

    def solve(self):
        for i in range(1, self.m+1):
            for j in range(1, self.n+1):
                if self.string1[i-1] == self.string2[j-1]:
                    self.t[i][j] = self.t[i-1][j-1] + 1
                else:
                    self.t[i][j] = max(self.t[i-1][j], self.t[i][j-1])
        for i in self.t:
            print(i)
        return self.t[-1][-1]


if __name__ == '__main__':
    a1 = 'abcd'
    a2 = 'abe'
    obj = Solution(a1, a2, len(a1), len(a2))
    ans = obj.solve()
    print(ans)
