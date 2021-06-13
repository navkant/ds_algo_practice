import sys

class Solution:
    def __init__(self):
        self.maximum = 1

    def longest_inc_subsequence(self, arr, n):
        if n == 1:
            return 1

        max_ending_here = 1

        for i in range(1, n):
            res = self.longest_inc_subsequence(arr, i)
            if arr[i-1] < arr[n-1] and res + 1 > max_ending_here:
                max_ending_here = res + 1

        self.maximum = max(max_ending_here, self.maximum)
        return max_ending_here


if __name__ == "__main__":
    a = [22, 10, 9, 33, 21, 50, 41, 60]
    N = len(a)
    obj = Solution()
    ans = obj.longest_inc_subsequence(a, N)
    print(f'ans is {ans}')