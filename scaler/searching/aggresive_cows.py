class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def is_possible(self, min_dist, arr, cows):
        prev = arr[0]
        cows -= 1
        j = 1

        while j < len(arr) and cows > 0:
            if arr[j] - prev >= min_dist:
                cows -= 1
                prev = arr[j]

            j += 1
        print()

        if cows == 0:
            return True
        else:
            return False

    def solve(self, A, B):
        A = sorted(list(set(A)))
        n = len(A)
        print(A)
        minn = A[0]
        maxx = A[0]

        for i in range(n):
            minn = min(A[i], minn)
            maxx = max(A[i], maxx)
        print(minn, maxx)
        start = 0
        end = (maxx - minn) // (B-1)

        while start <= end:
            mid = start + (end - start) // 2
            print(f'start {start} mid {mid} end {end}')
            if self.is_possible(mid, A, B):
                start = mid + 1
                ans = mid
            else:
                end = mid - 1

        return ans


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = 3

    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
