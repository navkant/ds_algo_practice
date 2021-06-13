class Solution:
    # @param A : list of list of integers
    # @return an integer
    def binary_search(self,arr):
        N = len(arr)
        low = 0
        high = N-1
        
        while low <= high:
            mid = low + (high-low)//2
            if mid == len(arr) - 1 and arr[mid] == 1:
                return mid
            elif mid == len(arr) - 1 and arr[mid] == 0:
                return -1

            if arr[mid] ==  1 and arr[mid-1] == 0:
                return mid
            elif arr[mid] == 0 and arr[mid+1] == 1:
                return mid + 1
            elif arr[mid] ==  1 and arr[mid-1] == 1:
                high = mid - 1
            elif arr[mid] ==  0 and arr[mid-1] == 0:
                low = mid + 1
            # return mid
        return mid

    def solve(self, A):
        i = 0
        while True:
            index_of_one = self.binary_search(A[i])
            max_vala_index = i
            if index_of_one != -1:
                break
        print(f'one is at index {index_of_one} in row {max_vala_index}')

        for x in range(max_vala_index+1, len(A)):
            if A[x][index_of_one] == 1:
                while A[x][index_of_one-1] != 0 and index_of_one>=0:
                    index_of_one -= 1
                    max_vala_index = x
            else:
                pass
        return max_vala_index


if __name__ == "__main__":
    a = [[0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1],
         [0, 0, 0, 1, 1, 1, 1, 1, 1]]

    obj = Solution()
    x = obj.solve(a)
    print(x)