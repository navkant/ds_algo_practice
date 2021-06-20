class Solution(object):
    def lps_recursive(self, string, i, j):
        if i == j:
            return 1

        if i + 1 == j:
            if string[i] == string[j]:
                return 2
            else:
                return 1

        if string[i] == string[j]:
            return 2 + self.lps_recursive(string, i+1, j-1)
        else:
            return max(self.lps_recursive(string, i+1, j),
                       self.lps_recursive(string, i, j-1))

    def lps_dp(self, string):
        n = len(string)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue

                if i + 1 == j:
                    if string[i] == string[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                    continue

                if string[i] == string[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        for row in dp:
            print(row)
        return dp[0][-1]

    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        lps_length = self.lps_dp(s)
        print(lps_length)
        ans = len(s) - lps_length
        print(f'ans is {ans}')
        return ans



if __name__ == '__main__':
    a = "leetcode"
    obj = Solution()
    obj.minInsertions(a)