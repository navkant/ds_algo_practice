class Solution:
    def __init__(self, str1, str2, length1, length2):
        self.str1 = str1
        self.str2 = str2
        self.n = length1
        self.m = length2
        self.memo = list()

        for i in range(self.n + 1):
            row = list()
            for j in range(self.m + 1):
                row.append(-1)
            self.memo.append(row)
        for x in self.memo:
            print(x)

    def solve(self):
        return self.get_lcs(self.n, self.m)

    def get_lcs(self, n, m):
        print(f'n: {n}, m: {m}')
        if n == 0 or m == 0:
            return 0

        if self.memo[n][m] != -1:
            return self.memo[n][m]
        else:
            if self.str1[n-1] == self.str2[m-1]:
                value = 1 + self.get_lcs(n-1, m-1)
                self.memo[n][m] = value
                return value

            if self.str1[n-1] != self.str2[m-1]:
                value = max(self.get_lcs(n-1, m), self.get_lcs(n, m-1))
                self.memo[n][m] = value
                return value

if __name__ == '__main__':
    a1 = 'abcdgrh'
    a2 = 'abedfhr'
    obj = Solution(a1, a2, len(a1), len(a2))
    ans = obj.solve()
    print(ans)
