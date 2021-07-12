class Solution:
    def __init__(self):
        pass

    def create_subsets(self, arr, n, ss, result):
        if n < 0:
            if ss and ss not in result:
                result.append(ss)
            return

        self.create_subsets(arr, n-1, ss + [arr[n]], result)
        self.create_subsets(arr, n-1, ss, result)

    def all_subsets(self, arr):
        ans = []
        self.create_subsets(arr, len(arr)-1, [], ans)
        print(f'ans is {ans}')

    def permutations_rec(self, arr, idx, all_perm):
        if idx == len(arr):
            all_perm.append([x for x in arr])
            return

        for i in range(idx, len(arr)):
            arr2 = arr.copy()
            if i != idx and arr2[i] == arr2[idx]:
                continue
            arr2[i], arr2[idx] = arr2[idx], arr2[i]
            self.permutations_rec(arr2, idx+1, all_perm)

    def all_permutations(self, arr):
        ans = []
        self.permutations_rec(arr, 0, ans)
        print(f'all permutations are {ans}')


if __name__ == '__main__':
    a = [1, 1, 2]
    obj = Solution()
    obj.all_permutations(a)
