class Solution:
    def solve(self, a):
        n = len(a)
        ans_arr = []
        stack = []

        for i in range(n):
            if not stack:
                ans_arr.append(-1)
                stack.append(i)
            else:
                if a[i] < a[stack[-1]]:
                    while stack and a[i] < a[stack[-1]]:
                        stack.pop()

                    if not stack:
                        ans_arr.append(-1)
                    else:
                        ans_arr.append(stack[-1])

                    stack.append(i)
                else:
                    ans_arr.append(stack[-1])
                    stack.append(i)

        return ans_arr


if __name__ == '__main__':
    a = [8, 1, 3, 4, 5, 2, 3, 6, 9]
    for i in range(len(a)):
        print(i, end=', ')
    print()
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print(f'{ans}')
