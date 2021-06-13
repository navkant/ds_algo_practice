class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        n = len(A)
        stack = []

        dct = {')': '(',
               '>': '<',
               ']': '[',
               '}': '{'}
        curr = 0
        ans = 0
        for i in A:
            if i in dct.values():
               stack.append((i, curr))
               curr = 0

            else:
                if stack and dct[i] == stack[-1][0]:
                    curr += 2 + stack[-1][1]
                    stack.pop()
                else:
                    stack = []
                    curr = 0

            ans = max(curr, ans)

        return ans


if __name__ == '__main__':
    a = '[{()}<()()>'
    obj = Solution()
    ans = obj.LBSlength(a)
    print(f'ans is {ans}')
