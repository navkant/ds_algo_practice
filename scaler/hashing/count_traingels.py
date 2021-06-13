class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        x_map = dict()
        y_map = dict()

        for i in range(n):
            if A[i] not in x_map:
                x_map[A[i]] = 1
            else:
                x_map[A[i]] += 1

        for i in range(n):
            if B[i] not in y_map:
                y_map[B[i]] = 1
            else:
                y_map[B[i]] += 1

        total_count = 0

        for j in range(n):
            point = (A[j], B[j])

            point_on_x = y_map.get(point[1], 0)
            point_on_y = x_map.get(point[0], 0)

            if point_on_x and point_on_y:
                point_on_x -= 1
                point_on_y -= 1

            total_count += point_on_y * point_on_x

        return total_count


if __name__ == '__main__':
    a = [1, 1, 2, 3, 3]
    b = [1, 2, 1, 2, 1]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')

