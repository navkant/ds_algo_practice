class Solution:
    def __init__(self):
        self.ans = -99999999999

    def max_sum_non_adjc(self, arr, n):
        if n == 0 or n == 1:
            if n == 1:
                return max(arr[0], arr[1])
            else:
                return arr[0]

        return max(self.max_sum_non_adjc(arr, n-1),
                   self.max_sum_non_adjc(arr, n-2) + arr[n])


if __name__ == '__main__':
    a = [0, 8, 4, 12, 2, 10]
    # a = [2, 3, 5, 0, 7, 10]
    N = len(a)
    obj = Solution()
    ans = obj.max_sum_non_adjc(a, N-1)
    print(f'ans is {ans}')
