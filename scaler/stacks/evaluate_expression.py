class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        n = len(A)
        stack = list()
        operators = ('/', '*', '-', '+')

        ans = 0
        for i in range(n):
            if A[i] not in operators:
                stack.append(int(A[i]))
            else:
                if A[i] == '/':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    val = top2 // top1
                    stack.append(val)
                elif A[i] == '*':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    val = top2 * top1
                    stack.append(val)
                elif A[i] == '+':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    val = top2 + top1
                    stack.append(val)
                elif A[i] == '-':
                    top1 = stack.pop()
                    top2 = stack.pop()
                    val = top2 - top1
                    stack.append(val)
        
        return stack[-1]


if __name__ == '__main__':
    a = ["4", "13", "5", "/", "+"]
    obj = Solution()
    ans = obj.evalRPN(a)
    print(f'ans is {ans}')
