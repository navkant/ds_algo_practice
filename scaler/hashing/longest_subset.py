import sys

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        if len(A) == 1:
            return 1
        n = len(A)
        B = sorted(list(A))
        ans = 0
        length = 0

        for i in range(1, n):
            if B[i] - B[i-1] == 1:
                length += 1
            else:

                ans = max(length, ans)
                length = 0

            if i == n-1:
                ans = max(length, ans)
        
        return ans + 1


if __name__ == "__main__":
    a = [6, 4, 5, 2, 3]
    obj = Solution()
    ans = obj.longestConsecutive(a)
    print(f'ans is {ans}')
