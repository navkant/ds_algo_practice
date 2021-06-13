class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        n = len(A)
        stack = list()

        dct = {')': '('}
        s = list()
        curr = 0
        ans = -99999999999

        for ind, i in enumerate(A):
            if i in dct.values():
                stack.append(i)
                s.append((i, curr))
                curr = 0
            elif stack and i in dct.keys() and dct[i] == stack[-1][0]:
                stack.pop()
                curr += s[-1][1] + 2
                s.pop()
                ans = max(ans, curr)
            else:
                s = []
                curr = 0

            print(f'{ind}: {i}: {stack} {ans} $$ {s}')

        print(ans)
        return ans


if __name__ == '__main__':
    string = ')()))(())((()))))'
    obj = Solution()
    obj.longestValidParentheses(string)
