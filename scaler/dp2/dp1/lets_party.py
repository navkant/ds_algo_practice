class Solution:
    def lets_party_recursive(self, people):
        mod = 10003
        if people <= 2:
            return people

        return self.lets_party_recursive(people-1) + (self.lets_party_recursive(people-2) * (people-1)) % mod

    def lets_party_itertive(self, peeps):
        mod = 10003
        dp = [0] * (peeps+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, peeps+1):
            dp[i] = dp[i-1] + (dp[i-2] * (i-1))

        return dp[-1] % mod

    def solve(self, A):
        ans2 = self.lets_party_itertive(A)
        print(f'iterative ans is {ans2}')

        ans = self.lets_party_recursive(A)
        print(f'recursive ans is {ans}')


if __name__ == '__main__':
    a = 50
    obj = Solution()
    obj.solve(a)
