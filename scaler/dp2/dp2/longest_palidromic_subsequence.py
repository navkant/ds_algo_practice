class Soltuion:
    def longest_palindromic_subsequence_recursive(self, string, start, end):
        # print(f'start {start}  end {end}')
        if start == end:
            return 1

        if start + 1 == end:
            if string[start] == string[end]:
                return 2
            else:
                return self.longest_palindromic_subsequence_recursive(string, start+1, end)

        if string[start] == string[end]:
            return 2 + self.longest_palindromic_subsequence_recursive(string, start+1, end-1)
        else:
            return max(self.longest_palindromic_subsequence_recursive(string, start+1, end),
                       self.longest_palindromic_subsequence_recursive(string, start, end-1))

    def longest_palindromic_subsequence_iterative(self, string):
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for row in dp:
            print(row)

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue

                elif i+1 == j:
                    if string[i] == string[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else:
                    if string[i] == string[j]:
                        dp[i][j] = 2 + dp[i+1][j-1]
                    else:
                        dp[i][j] = max(dp[i+1][j],
                                       dp[i][j-1])
        print()
        for row in dp:
            print(row)

        return dp[0][-1]


    def solve(self, s):
        n = len(s)
        ans = self.longest_palindromic_subsequence_recursive(s, 0, n-1)
        print(f'recursive ans is {ans}')
        ans = self.longest_palindromic_subsequence_iterative(s)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = "leetcode"
    obj = Soltuion()
    obj.solve(a)
