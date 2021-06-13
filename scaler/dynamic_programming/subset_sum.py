class Solution:
    def __init__(self):
        pass

    def subset_sum_recursive(self, array, n, s):
        if n < 0:
            if s == 0:
                return True
            return False

        if s == 0:
            return True

        return self.subset_sum_recursive(array, n-1, s - array[n]) or self.subset_sum_recursive(array, n-1, s)

    # def subset_sum_bottom_up(self, array, summ):
    #     n = len(array)

    def solve(self, arr, summ):
        return self.subset_sum_recursive(arr, len(a)-1, summ)


if __name__ == '__main__':
    a = [3, 34, 4, 12, 5, 2]
    obj = Solution()
    ans = obj.solve(a, 30)
    print(f'ans is {ans}')