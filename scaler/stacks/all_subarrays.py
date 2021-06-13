import sys


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        stack = list()

        ans = sys.maxsize * -1
        for i in range(n):
            while stack:
                ans = max(ans, stack[-1] ^ A[i])
                print(stack, A[i])
                print(ans)
                if A[i] < stack[-1]:
                    break
                stack.pop()

            stack.append(A[i])


        return ans


if __name__ == '__main__':
    a = [5, 4, 3, 7]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')