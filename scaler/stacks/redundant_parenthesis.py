class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        
        stack = []
        # op_stack = []

        for i in A:
            if i == '(' or i in ['-', '+', '*', '/']:
                stack.append(i)

            elif i == ')':
                top = stack.pop()
                if top not in ['-', '+', '*', '/']:
                    return 1
                else:
                    stack.pop()

        return 0

if __name__ == "__main__":
    a = "(a+(a+b))"
    obj = Solution()
    ans = obj.braces(a)
    print(f'ans is {ans}')
