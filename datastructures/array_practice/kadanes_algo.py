class Solution:
    def get_maximum_sum(self, array):
        max_ending_here = max_so_far = 0
        for i in range(len(array)):
            max_ending_here = max_ending_here + array[i]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            else:
                pass
        return max_so_far

    def solve(self, a):
        ans = self.get_maximum_sum(a)
        print(f'ans is {ans}')


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -3, 1, 5, -3]
    obj = Solution()
    obj.solve(arr)
