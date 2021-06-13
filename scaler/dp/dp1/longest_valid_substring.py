class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        n = len(A)
        ans = 0
        data = {')': '(',
                '}': '{',
                ']': '['}
        s = []
        curr = 0

        for i in A:
            print(s, curr, ans)
            if i in data.values():
                s.append((i, curr))
                curr = 0
            elif len(s) > 0 and data[i] == s[-1][0]:
                curr += 2 + s[-1][1]
                s.pop()
            else:
                s = []
                curr = 0
            ans = max(ans, curr)

        return ans


if __name__ == '__main__':
    a = '()((()))))'
    obj = Solution()
    ans = obj.LBSlength(a)
    print(f'ans is {ans}')
