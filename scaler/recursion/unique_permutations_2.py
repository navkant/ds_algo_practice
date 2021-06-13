class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def rec_func(self, arr, idx, ans):
        print(f'arr: {arr} idx {idx}')
        if idx == len(arr):
            ans.append(arr)
            return

        for i in range(idx, len(arr)):
            if i != idx and arr[idx] == arr[i]:
                continue
            arr2 = arr.copy()
            arr2[i], arr2[idx] = arr2[idx], arr2[i]

            self.rec_func(arr2, idx+1, ans)
            # arr[i], arr[idx] = arr[idx], arr[i]

    def solve(self, A):
        res = []
        self.rec_func(A, 0, res)

        print(len(res))
        for i in res:
            print(i)
        return res


if __name__ == '__main__':
    a = [2850, 286, 155]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
