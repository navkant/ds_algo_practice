class Solution:
    def ge_triangels(self, Ax, By):
        all_points = list(zip(Ax, By))

        n = len(Ax)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    print([(all_points[i][0], all_points[i][1]), (all_points[j][0], all_points[j][1]), (all_points[k][0], all_points[k][1])])
        return 0

if __name__ == "__main__":
    a = ['x1', 'x2', 'x3', 'x4']
    b = ['y1', 'y2', 'y3', 'y4']
    obj = Solution()
    ans = obj.ge_triangels(a, b)
