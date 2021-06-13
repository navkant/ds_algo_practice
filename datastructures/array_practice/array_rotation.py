class Solution:
    # @param A : list of list of integers
    def reverse_array(self, arr):
        mid = len(arr)//2
        for j in range(mid):
            last_index = len(arr) - j -1
            arr[j], arr[last_index] = arr[last_index], arr[j]
        return arr
            
        
    def solve(self, A):
        for i in range((len(A))):
            for j in range(i, len(A[i])):
                if i == j:
                    continue
                else:
                    A[i][j], A[j][i] = A[j][i], A[i][j]
        print('transpose is')
        for i in A:
            print(i)
        print('-------------')
        for i in range(len(A)):
            A[i] = self.reverse_array(A[i])
            
        return A


if __name__ == "__main__":
    # a = [[1,2,3, 10], [4,5,6, 11], [7,8,9, 12], [13, 14, 15, 16]]
    a = [[1,2,3], [4,5,6], [7,8,9]]
    for i in a:
        print(i)
    print('***********')
    obj = Solution()
    ans = obj.solve(a)
    for i in ans:
        print(i)