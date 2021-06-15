class Solution:
    def __init__(self):
        self.max_length = float('-inf')

    def lcsb_recursive2(self, str1, str2, i, j, sub_length):
        if i < 0 or j < 0:
            return 0

        if str1[i] == str2[j]:
            return 1 + self.lcsb_recursive2(str1, str2, i-1, j-1, sub_length+1)
        else:
            return max(self.lcsb_recursive2(str1, str2, i-1, j, 0),
                       self.lcsb_recursive2(str1, str2, i, j-1, 0))

    def lcsb_dp(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
        for row in dp:
            print(row)
        return max(max(row) for row in dp)

    def lcsb(self, str1, str2):
        ans = self.lcsb_recursive2(str1, str2, len(str1)-1, len(str2)-1, 0)
        print(f'ans is {ans}')
        ans = self.lcsb_dp(str1, str2)
        print(f'iterative ans is {ans}')


if __name__ == '__main__':
    a = 'abcdaf'
    b = 'acbcf'
    obj = Solution()
    obj.lcsb(a, b)