class Solution:

    def insertion_sort(self, arr):
        n = len(arr)

        for i in range(1, n):
            temp = arr[i]

            for k in range(i, -1, -1):
                if arr[k-1] > temp:
                    arr[k] = arr[k-1]
                else:
                    break
            arr[k] = temp
            print(arr)


if __name__ == '__main__':
    a = [5, 6, 11, 12, 13]
    obj = Solution()
    ans = obj.insertion_sort(a)
    print(f'ans is {ans}')
