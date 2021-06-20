class Solution:
    def is_palindrome(self, string):
        print(string)
        n = len(string)
        if n == 1:
            return 1
        i = 0
        j = len(string) - 1

        while j > i:
            if string[i] == string[j]:
                pass
            else:
                return False
            i += 1
            j -= 1
        return True

    def num_palindrom_partition(self, string, i, j):
        print(f'i: {i} j: {j}')
        if i >= j:
            return 0

        if self.is_palindrome(string[i:j+1]):
            return 0

        min_partition = float('inf')
        for k in range(i, j):
            left = self.num_palindrom_partition(string, i, k)
            right = self.num_palindrom_partition(string, k+1, j)
            curr = 1 + left + right
            min_partition = min(curr, min_partition)
        return min_partition

    def num_palindrom_partition_memo(self, string, i, j, dp):
        print(f'i: {i} j: {j}')
        if i >= j:
            return 0

        if self.is_palindrome(string[i:j+1]):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        min_partition = float('inf')
        for k in range(i, j):
            left = self.num_palindrom_partition_memo(string, i, k, dp)
            right = self.num_palindrom_partition_memo(string, k+1, j, dp)
            curr = 1 + left + right
            min_partition = min(curr, min_partition)
        dp[i][j] = min_partition
        return min_partition

    def solve(self, string):
        n = len(string)
        dp = [[-1 for j in range(n+1)] for i in range(n)]
        ans = self.num_palindrom_partition_memo(string, 0, n, dp)
        print(f'ans is {ans}')


if __name__ == '__main__':
    s = 'bananas'
    obj = Solution()
    obj.solve(s)
    # ans = obj.is_palindrome('ba')
    # print(f'ans is {ans}')