class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    
    def rec_func(self, arr, n, output, ans):
        if n == len(arr)-1 and output not in ans:
            ans.append(output)
            return

        output2 = output.copy()
        self.rec_func(arr, n+1, output, ans)
        output2.append(arr[n+1])
        self.rec_func(arr, n+1, output2, ans)


    def subsets(self, A):
        n = len(A)
        output = []
        ans = []
        self.rec_func(A, -1, output, ans)
        # ans.remove([])
        # ans = sorted(ans, key=lambda x: x[0])
        # ans.insert(0, [])
        ans = sorted(ans)
        print(ans)


if __name__ == '__main__':
    a = [1, 2, 3]
    obj = Solution()
    ans = obj.subsets(a)
    print(f'ans is {ans}')
