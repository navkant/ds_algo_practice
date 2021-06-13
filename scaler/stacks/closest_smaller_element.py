class Solution:
    def solve(self, a):
        n = len(a)
        stack = []
        ans = []

        for i in range(n):
            if not stack:
                ans.append(-1)
            else:
                while stack and a[stack[-1]] >= a[i]:
                    stack.pop()

                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)

            stack.append(i)

        return ans


if __name__ == '__main__':
    a = [1, 1]
    for i in range(len(a)):
        print(i, end=', ')
    print()
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print(f'{ans}')
