class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def binary_search(self, arr, key):
        print(arr)
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    def solve(self, A, B):
        j = len(A[0]) - 1 
        for i in range(len(A)):
            if A[i][j] == B:
                return (((i+1)*1009) + (j+1))
            elif A[i][j] > B:
                column = self.binary_search(A[i], B)
                if column != -1:
                    return (((i+1) * 1009) + (column+1))
                else:
                    continue
            else:
                continue
        return -1

if __name__ == '__main__':
    arr = [[1, 2, 5, 7, 10, 11, 12, 13, 14, 17, 19, 20, 23, 24, 27, 28, 29, 30, 31, 32, 34, 35, 37, 39, 40, 41, 42, 43, 45, 46, 47, 50, 53],
           [4, 6, 8, 10, 11, 13, 15, 18, 20, 21, 24, 25, 27, 30, 33, 36, 37, 40, 41, 42, 43, 44, 45, 48, 51, 54, 55, 56, 59, 62, 63, 65, 66],
           [7, 8, 11, 14, 17, 19, 22, 25, 27, 29, 30, 31, 34, 36, 37, 40, 42, 44, 45, 48, 49, 52, 55, 58, 60, 63, 66, 69, 70, 73, 76, 78, 79],
           [10, 11, 13, 17, 19, 22, 23, 26, 30, 31, 33, 36, 38, 41, 43, 45, 46, 48, 49, 50, 53, 55, 58, 59, 63, 66, 69, 70, 71, 75, 77, 80, 82],
           [13, 16, 17, 20, 22, 23, 26, 27, 31, 32, 36, 39, 41, 44, 47, 50, 52, 55, 58, 61, 63, 66, 68, 71, 72, 75, 77, 78, 80, 81, 82, 84, 85],
           [15, 19, 22, 25, 28, 29, 31, 34, 36, 38, 41, 42, 44, 45, 50, 51, 55, 58, 60, 64, 66, 69, 72, 75, 77, 80, 83, 84, 86, 89, 90, 93, 96],
           [16, 21, 23, 28, 29, 32, 34, 36, 38, 39, 42, 45, 47, 48, 52, 54, 57, 60, 62, 66, 69, 72, 74, 76, 79, 81, 84, 86, 88, 91, 93, 96, 99]]
    k = 91
    obj = Solution()
    ans = obj.solve(arr, k)
    print('ans: ', ans)