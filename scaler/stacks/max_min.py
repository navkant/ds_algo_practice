class Solution:
    def closest_smaller_left(self, a):
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

    def closest_smaller_right(self, a):
        n = len(a)
        stack = []
        ans = []

        for i in range(n-1, -1, -1):
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

        return ans[::-1]

    def closest_bigger_left(self, a):
        n = len(a)
        stack = []
        ans = []

        for i in range(n):
            if not stack:
                ans.append(-1)
            else:
                while stack and a[i] >= a[stack[-1]]:
                    stack.pop()
                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(i)
        return ans

    def closes_bigger_right(self, a):
        n = len(a)
        stack = []
        ans = []

        for i in range(n-1, -1, -1):
            if not stack:
                ans.append(-1)
            else:
                while stack and a[i] > a[stack[-1]]:
                    stack.pop()

                if stack:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
            stack.append(i)

        return ans[::-1]

    def solve(self, A):
        n = len(A)
        left_mins = self.closest_smaller_left(A)
        print(left_mins)
        right_mins = self.closest_smaller_right(A)
        print(right_mins)
        left_max = self.closest_bigger_left(A)
        print(left_max)
        right_max = self.closes_bigger_right(A)
        print(right_max)

        ans = 0
        for i in range(n):
            maxx = 0
            closest_smaller_left = left_mins[i]
            closest_smaller_right = right_mins[i]
            closest_bigger_left = left_max[i]
            closest_bigger_right = right_max[i]

            # x1 number of start points when ith element is minimumm element
            if closest_smaller_left == -1:
                x1 = i + 1
            else:
                x1 = i - closest_smaller_left

            # x2 number of end points when ith element is minimum element
            if closest_smaller_right == -1:
                x2 = n - i
            else:
                x2 = closest_smaller_right - i

            # x3 number of start points when ith element is maximum element
            if closest_bigger_left == -1:
                x3 = i + 1
            else:
                x3 = i - closest_bigger_left

            # x4 number of end points when ith element is minimum element
            if closest_bigger_right == -1:
                x4 = n - i
            else:
                x4 = closest_bigger_right - i

            ans += (A[i] * (x3 * x4)) - (A[i] * (x2 * x1))

        return ans


if __name__ == '__main__':
    a = [4, 7, 3, 8]
    obj = Solution()
    ans = obj.solve(a)
    print(f'{ans}')
