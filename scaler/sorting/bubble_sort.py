class Solution:
    def bubble_sort(self, arr):
        n = len(arr)

        for i in range(n):
            swap = False
            for j in range(1, n-i):
                if arr[j] < arr[j-1]:
                    swap = True
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    print(arr)
            if not swap:
                break

        return arr


if __name__ == '__main__':
    a = [5, 6, 11, 12, 13]  # [13, 12, 11, 6, 5]
    obj = Solution()
    ans = obj.bubble_sort(a)
    print(f'ans is {ans}')