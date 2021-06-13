class Solution:
    # @param A : string
    # @return a strings
    def convert(self, expression):
        n = len(expression)
        stack = list()
        ans = ''

        precedence = {'^': 4,
                      '*': 3,
                      '/': 3,
                      '+': 2,
                      '-': 2}

        for i in range(n):
            print(i, stack, ans, end=' ')
            if expression[i] not in ('+', '-', '*', '^', '/', ')', '('):
                ans += expression[i]

            elif expression[i] == '(':
                stack.append(expression[i])

            elif (not stack or stack[-1] in ('(', ')')) and expression[i] in ('+', '-', '*', '/', '^'):
                stack.append(expression[i])

            elif (stack and stack[-1] in ('+', '-', '*', '/', '^')) and expression[i] in ('+', '-', '*', '/', '^'):
                while (stack and stack[-1] in ('+', '-', '*', '/', '^')) and precedence[expression[i]] <= precedence[stack[-1]]:
                    print('hey')
                    top = stack.pop()  # 1
                    ans += top
                stack.append(expression[i])
            elif expression[i] == ')':
                while stack[-1] != '(':
                    top = stack.pop()
                    ans += top
                stack.pop()
            print()

        while stack and stack[-1] in ('+', '-', '*', '/', '^'):
            ans += stack.pop()

        return ans

    def solve(self, A):
        return self.convert(A)


if __name__ == '__main__':
    a = "a+b*(c^d-e)^(f+g*h)-i"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
