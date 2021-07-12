import math


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def is_sqr(self, x):
        print(f'check {x}')
        r = int(math.sqrt(x))
        if r ** 2 == x:
            return True
        else:
            return False

    # def rec_func(self, arr, idx, ans):
    #     if idx == len(arr):
    #         ans.append(1)
    #         return
    #
    #     for i in range(idx, len(arr)):
    #         if i != idx and arr[idx] == arr[i]:
    #             continue
    #         arr2 = arr.copy()
    #         arr2[i], arr2[idx] = arr2[idx], arr2[i]
    #
    #         if idx == 0 or (idx > 0 and self.is_sqr(arr2[idx] + arr2[idx - 1])):
    #             self.rec_func(arr2, idx + 1, ans)
    def rec_func(self, arr, idx, ans, r):
        if idx == len(arr):
            prev_length = len(r)
            r.add(tuple(arr))
            new_length = len(r)
            if new_length > prev_length:
                ans.append(1)
            return

        for i in range(idx, len(arr)):
            if i != idx and arr[idx] == arr[i]:
                if self.is_sqr(arr2[idx] + arr2[idx-1]):
                    self.rec_func(arr2, idx+1, ans, r)
                continue

            arr2 = arr.copy()
            arr2[i], arr2[idx] = arr2[idx], arr2[i]
            if idx == 0 or (idx > 0 and self.is_sqr(arr2[idx] + arr2[idx-1])):
                self.rec_func(arr2, idx+1, ans, r)

    def solve(self, A):
        if len(A) == 1:
            return 0
        a = list()
        res = set()
        self.rec_func(A, 0, a, res)
        # print(a)
        return sum(a)


if __name__ == '__main__':
    A = [ 2850, 286, 155 ]
    obj = Solution()
    ans = obj.solve(A)
    print(f'ans is {ans}')
