class Solution:
    def get_zee_value(self, string):
        n = len(string)
        z = [-1] * n
        z[0] = n

        l = 0
        r = 0

        for i in range(1, n):
            if i > r:
                l = r = i
                while r < n and string[r] == string[r-l]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                if i + z[i - l] <= r:
                    z[i] = z[i-l]
                else:
                    l = i
                    while r < n and string[r] == string[r-l]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        print(z)
        return z

    def solve(self, s):
        n = len(s)
        zee_value = self.get_zee_value(s)

        for i in range(1, n):
            if i + zee_value[i] == n:
                return i
        print('hello')
        return n


if __name__ == '__main__':
    s = 'abababababb'
    obj = Solution()
    ans = obj.solve(s)
    print(f'ans is {ans}')
