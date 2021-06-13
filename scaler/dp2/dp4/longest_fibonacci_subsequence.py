class Solution:
    # @param A : list of integers
    # @return an integer

    def __init__(self):
        self.maximum = 99999999999

    def lifs(self, arr):
        n = len(arr)
        arr = [[i, 1] for i in arr]
        print(arr)

        hash = {arr[0][0]: 1}


    def solve(self, A):
        ans = self.lifs(A)
        print(f'ans is {ans}')

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    obj = Solution()
    ans = obj.solve(a)
