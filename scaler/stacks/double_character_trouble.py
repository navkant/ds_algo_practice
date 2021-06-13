class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        stack = list()

        for i in range(n):
            if not stack:
                stack.append(A[i])
            else:
                if stack[-1] == A[i]:
                    while stack[-1] == A[i]:
                        stack.pop()
                else:
                    stack.append(A[i])

        return ''.join(stack)


if __name__ == '__main__':
    a = 'abccbc'
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
