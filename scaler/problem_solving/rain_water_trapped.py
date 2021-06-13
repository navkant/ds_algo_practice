import sys

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        global_maxx = sys.maxsize * -1
        global_i_max = 0

        for i in range(len(A)):
            if A[i] > global_maxx:
                global_maxx = A[i]
                global_i_max = i
            else:
                pass
        print(global_i_max)
        water_trapped = 0
        if global_i_max != n-1:
            print('in middle')
            local_maxx = A[0]
            for i in range(1, global_i_max+1):
                current_max = min(local_maxx, global_maxx)
                if current_max > A[i]:
                    print(f'water trapped at index {i}')
                    water_trapped += (current_max - A[i])
                else:
                    pass
                local_maxx = max(A[i], local_maxx)
            local_maxx = A[-1]
            for i in range(n-1, global_i_max-1, -1):
                current_max = min(local_maxx, global_maxx)
                if current_max > A[i]:
                    water_trapped += (current_max - A[i])
                else:
                    pass
                local_maxx = max(A[i], local_maxx)
        else:
            print('at last')
            local_maxx = A[0]
            for i in range(1, n):
                current_max = min(local_maxx, global_maxx)
                if current_max > A[i]:
                    water_trapped += (current_max - A[i])
                else:
                    pass
                local_maxx = max(A[i], local_maxx)

        return water_trapped


if __name__ == '__main__':
    a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    obj = Solution()
    ans = obj.trap(a)
    print(f'ans is : {ans}')
