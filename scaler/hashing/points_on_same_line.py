class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def get_gcd(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        else:
            return self.get_gcd(b, a % b)

    def solve(self, A, B):
        n = len(A)
        slopes = dict()

        ans = -9999999999

        for i in range(n):
            x1, y1 = A[i], B[i]
            points_map = dict()
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = A[j], B[j]

                if x1 != x2:
                    num = y2 - y1
                    deno = x2 - x1
                    sign = num * deno
                    gcd = self.get_gcd(abs(num), abs(deno))
                    num //= gcd
                    deno //= gcd
                    if num != 0:
                        slope_str = '{0}/{1}'.format(abs(num), abs(deno))  # f'{abs(num)}/{abs(deno)}'
                    else:
                        slope_str = '0'
                else:
                    sign = 1
                    slope_str = 'inf'

                if sign < 0:
                    sign = '-'
                else:
                    sign = '+'

                if (sign, slope_str) not in points_map:
                    points_map[(sign, slope_str)] = 2
                else:
                    points_map[(sign, slope_str)] += 1

            for k, v in points_map.items():
                print(k, v)
            print()
            ans = max(max(points_map.values()), ans)

        # for k, v in slopes.items():
        #     print(k, v)

        return ans


if __name__ == '__main__':
    a = [48, 45, -3, 7, -25, 38, 2, 13, 13, 18, -44, 34, -27, -46, 48, -39, -41, -32, -16, 17, -6, 44, -28, -44, -6, -43, -16, 30, -3, -27, 32, 38, -26, 20, 4, -44, -37]
    b = [47, -42, 41, 22, -4, -35, -45, -22, 5, -20, 21, -13, 47, 32, -48, 47, 17, -23, 30, -30, 37, 42, 44, 23, 1, -40, -9, 34, -34, 49, 16, -35, 2, -19, 31, 23, -37]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
