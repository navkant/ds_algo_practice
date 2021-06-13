class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        array = list()

        i = 0
        for k in range(0, len(A)):
            row = list()
            j = k
            while j >= 0:
                row.append(A[i][j])
                j -= 1
                i += 1
            array.append(row)
            i=0
        
        j = len(A) - 1
        for k in range(1, len(A)):
            row = list()
            i = k
            while i <= len(A)-1:
                row.append(A[i][j])
                i += 1
                j -= 1
            array.append(row)
            j = len(A) - 1

        return array


if __name__ == '__main__':
    a = [[1,2,3,10],
         [4,5,6,11],
         [7,8,9,12],
         [13,14,15,16]]

    obj = Solution()
    x = obj.diagonal(a)
    for i in x:
        print(i)
