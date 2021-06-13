class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lo, hi = 1, len(A)
        n = len(A)
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo)//2
            s = sum(A[:mid])
            print(f'lo {lo} mid {mid} hi {hi} sum {s}')
            if s > B:
                hi = mid-1
                continue
            for i in range(mid, n):
                s += A[i]-A[i-mid]
                if s > B:
                    hi = mid-1
                    break
            else:
                lo = mid+1
                ans = mid

        return ans


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = 10
    obj = Solution()
    ans = obj.solve(a, 10)
    print(f'ans is {ans}')
