import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        i = 0
        j = n - 1

        ans = sys.maxsize * -1

        while i < j:
            width = j - i
            height = min(A[i], A[j])
            area = width * height
            ans = max(area, ans)

            if A[j] < A[i]:
                j -= 1
            else:
                i += 1

        return ans

if __name__ == "__main__":
    a = [1, 5, 4, 3]
    obj = Solution()
    ans = obj.maxArea(a)
    print(f'ans is {ans}')