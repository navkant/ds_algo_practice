class Solution:
    def selection_sort(self, arr):
        n = len(arr)

        for i in range(n):
            minn = arr[i]
            min_index = i
            for j in range(i, n):
                if arr[j] < minn:
                    minn = arr[j]
                    min_index = j
            print(arr)
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr


if __name__ == '__main__':
    a = [94, 87, 100, 11, 23, 98, 17, 35, 43, 66, 34, 53, 72, 80, 5, 34, 64, 71, 9, 16, 41, 66, 96]
    obj = Solution()
    ans = obj.selection_sort(a)
    print(f'ans is {ans}')