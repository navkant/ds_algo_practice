class Solution:
    def __init__(self):
        pass

    def coin_sum_recursive_all_combinations(self, arr, n, summ, elements):
        if summ == 0:
            print(f'summ {summ} elements: {elements}')
            return 1

        if summ < 0:
            return 0

        ans = 0
        for i in range(n):
            elements2 = elements.copy()
            elements2.append(arr[i])
            ans += self.coin_sum_recursive_all_combinations(arr, n, summ-arr[i], elements2)

        return ans

    def solve(self, arr, amount):
        print(f'recursive ans is {self.coin_sum_recursive_all_combinations(arr, len(arr), amount, [])}')


if __name__ == '__main__':
    a = [1, 3, 4]
    b = 5
    obj = Solution()
    obj.solve(a, b)
