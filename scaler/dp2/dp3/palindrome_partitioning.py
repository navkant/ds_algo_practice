class Solution:

    def get_palindrome_dp(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        for row in dp:
            print(row)

        for i in range(n-2, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue

                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True

                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        pass
        print()
        for row in dp:
            print(row)

        return dp

    def get_min_partitions(self, string):
        n = len(string)
        pal_dp = self.get_palindrome_dp(string)

        ans = [i for i in range(n)]
        if string[0] == string[1]:
            ans[1] = 0

        for i in range(2, n):
            if pal_dp[0][i]:
                ans[i] = 0
                continue

            for j in range(i+1):
                if pal_dp[j][i]:
                    ans[i] = min(ans[i], ans[j-1]+1)

        print()
        print(ans)
        return ans[-1]

    def minCut(self, A):
        if len(A) == 1:
            return 0
        return self.get_min_partitions(A)


if __name__ == '__main__':
    a = "bebdeeedaddecebbbbbabebedc"
    obj = Solution()
    ans = obj.minCut(a)
    print(f'ans is {ans}')