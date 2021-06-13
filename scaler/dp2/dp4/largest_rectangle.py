import sys


class LargestRectangle:
    def nearest_minimum_left(self, a):
        n = len(a)
        ans_arr = []
        stack = []

        for i in range(n):
            if not stack:
                ans_arr.append(-1)
                stack.append(i)
            else:
                if a[i] > a[stack[-1]]:
                    ans_arr.append(stack[-1])
                    stack.append(i)
                else:
                    while stack and a[i] <= a[stack[-1]]:
                        stack.pop()

                    if not stack:
                        ans_arr.append(-1)
                    else:
                        ans_arr.append(stack[-1])
                    stack.append(i)
        return ans_arr

    def nearest_minimum_right(self, a):
        n = len(a)
        ans_arr = []
        stack = []

        for i in range(n-1, -1, -1):
            if not stack:
                ans_arr.append(-1)
                stack.append(i)
            else:
                if a[i] > a[stack[-1]]:
                    ans_arr.append(stack[-1])
                    stack.append(i)
                else:
                    while stack and a[i] <= a[stack[-1]]:
                        stack.pop()

                    if not stack:
                        ans_arr.append(-1)
                    else:
                        ans_arr.append(stack[-1])
                    stack.append(i)
        return ans_arr[::-1]

    def largest_rectangle(self, a):
        n = len(a)
        left_mins = self.nearest_minimum_left(a)
        right_mins = self.nearest_minimum_right(a)
        # print(a)
        # print(left_mins)
        # print(a)
        # print(right_mins)

        max_area = 0

        for i in range(len(a)):
            left_min = left_mins[i]
            right_min = right_mins[i]

            height = a[i]

            if left_min == -1 and right_min == -1:
                width = n
            elif right_min == -1:
                width = n - left_min - 1
            elif left_min == -1:
                width = right_min
            else:
                width = right_min - left_min - 1

            area = height * width
            # print(area, end=' ')
            max_area = max(max_area, area)

        return max_area

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        n = len(A[0])
        m = len(A)

        for i in range(1, m):
            for j in range(n):
                if A[i][j] == 0:
                    continue
                A[i][j] = A[i][j] + A[i-1][j]

        maxx_area = sys.maxsize * -1
        obj = LargestRectangle()
        for row in A:
            current_area = obj.largest_rectangle(row)
            maxx_area = max(maxx_area, current_area)

        return maxx_area


if __name__ == '__main__':
    a = [[1, 1, 1, 1, 0, 1, 1],
         [0, 1, 1, 1, 1, 1, 0],
         [1, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 1, 1, 1]]
    obj = Solution()
    ans = obj.maximalRectangle(a)
