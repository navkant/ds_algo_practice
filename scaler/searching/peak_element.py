class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        start = 0
        end = n - 1

        while start <= end:
            if start == end:
                return A[end]
            mid = start + (end - start) // 2
            print(f'start {start} mid {mid} end {end} ')
            if A[mid-1] <= A[mid] >= A[mid+1]:
                return A[mid]
            elif A[mid-1] > A[mid]:
                end = mid -1
            else:
                start = mid + 1


if __name__ == '__main__':
    a = [2, 3]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans: {ans}')
