class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        n = len(A)
        arr = list(A)

        for i in range(B):
            minn = arr[i]
            min_index = i

            for j in range(i, n):
                if arr[j] < minn:
                    minn = arr[j]
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr)

        return minn


if __name__ == '__main__':
    a = [94, 87, 100, 11, 23, 98, 17, 35, 43, 66, 34, 53, 72, 80, 5, 34, 64, 71, 9, 16, 41, 66, 96]
    b = 19
    obj = Solution()
    ans = obj.kthsmallest(a, b)
    print(f'ans is {ans}')