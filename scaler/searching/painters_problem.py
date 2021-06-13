import sys


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        maxx = sys.maxsize * -1
        total_length = 0

        pref_arr = [C[0]]

        for i in C:
            total_length += i
            maxx = max(maxx, i)

        maxx_time = total_length * B
        minn_time = maxx * B
        total_paint_time = maxx_time

        if A >= len(C):
            return maxx * B

        while minn_time < maxx_time:
            mid = minn_time + ((maxx_time - minn_time)//2)
            print(f'mid {mid}')
            paint_time = 0
            painter_count = 1
            i = 0
            max_paint_time = 0
            while i < len(C):
                paint_time += C[i] * B
                print(f'i {i}: minn {minn_time} maxx {maxx_time} p_time {paint_time} painter {painter_count}')
                if max_paint_time == mid:
                    painter_count += 1
                    max_paint_time = max(max_paint_time, paint_time)
                    if painter_count > A:
                        print('painter limit exceeded')
                        break
                    else:
                        pass
                    paint_time = 0
                elif paint_time > mid:
                    painter_count += 1
                    paint_time -= C[i] * B
                    max_paint_time = max(max_paint_time, paint_time)
                    if painter_count > A:
                        print('painter limit exceeded')
                        paint_time += C[i] * B
                        max_paint_time = max(max_paint_time, paint_time)
                        break
                    else:
                        pass

                    paint_time = 0
                    continue
                else:
                    pass
                    max_paint_time = max(max_paint_time, paint_time)
                i += 1

            print(max_paint_time)
            if max_paint_time <= mid:
                maxx_time = mid-1
            elif max_paint_time > mid:
                minn_time = mid+1

            if i == len(C):
                total_paint_time = min(total_paint_time, max_paint_time)

        print(f'total time {total_paint_time} max paint time {max_paint_time}')

        return max_paint_time


if __name__ == '__main__':
    a = 7
    b = 10
    c = [ 452, 305, 314, 443, 826, 163, 433, 51, 372 ]
    obj = Solution()
    ans = obj.paint(a, b, c)
    print(f'ans is {ans}')
