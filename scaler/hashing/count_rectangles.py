class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        points_map = dict()

        for i in range(n):
            if (A[i], B[i]) not in points_map:
                points_map[(A[i], B[i])] = 1
            else:
                pass

        count = 0

        for i in range(n):
            for j in range(i+1, n):
                first_point = (A[i], B[i])
                second_point = (A[j], B[j])

                if A[i] != A[j] and B[i] != B[j]:
                    third_point = (second_point[0], first_point[1])
                    fourth_point = (first_point[0], second_point[1])
                    print(first_point, second_point, third_point, fourth_point)

                    if third_point in points_map and fourth_point in points_map:
                        count += 1
                    else:
                        pass

        return count


if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 3]
    b = [1, 2, 1, 2, 1, 2]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
