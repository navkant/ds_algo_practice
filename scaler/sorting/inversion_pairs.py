class Solution:
    def __init__(self):
        pass

    def merge_sort(self, arr, start, end):
        print(f'start {start} end {end}')
        if start == end:
            return 0

        mid = start + (end - start) // 2
        print(f'mid {mid}')
        count = self.merge_sort(arr, start, mid) + self.merge_sort(arr, mid+1, end)
        j = mid + 1
        for i in range(start, mid+1):
            while j <= end and i < j and arr[i] > arr[j]:
                j += 1
            count += j - (mid + 1)

        self.merge(arr, start, mid, end)
        return count

    def merge(self, a, start, mid, end):
        n1 = (mid - start + 1)
        n2 = (end - mid)
        L = [0] * n1
        R = [0] * n2
        for i in range(n1):
            L[i] = a[start + i]
        for j in range(n2):
            R[j] = a[mid + 1 + j]
        i = 0
        j = 0
        for k in range(start, end + 1):
            if j >= n2 or (i < n1 and L[i] <= R[j]):
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    obj = Solution()
    ans = obj.merge_sort(a, 0, len(a)-1)
    print(f'ans is {ans}')
