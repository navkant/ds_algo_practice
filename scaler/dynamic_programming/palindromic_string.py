class Solution:
    def check_palindrome(self, string, i, j):
        if i == j:
            return True

        if i+1 == j:
            if string[i] == string[j]:
                return True
            else:
                return False

        if string[i] == string[j] and self.check_palindrome(string, i+1, j-1):
            return True
        else:
            return False

    def solve_recursive(self, string):
        return self.check_palindrome(string, 0, len(string)-1)

    def bottom_up(self, string):
        n = len(string)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                print(i, j)
                if i == j:
                    continue
                elif j == i + 1:
                    if string[i] == string[j]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if string[i] == string[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = False

        for row in dp:
            print(row)
        return dp[0][n-1]


if __name__ == '__main__':
    a = 'abba'
    obj = Solution()
    ans = obj.solve_recursive(a)
    print(f'ans is {ans}')
    ans2 = obj.bottom_up(a)
    print(f'ans is {ans2}')
