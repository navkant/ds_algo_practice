class Solution:
    def __init__(self):
        pass

    def merge_sort(self, arr, start, end):
        print(f'start {start} end {end}')
        if start == end:
            return [arr[start]]

        mid = start + (end - start) // 2
        print(f'mid {mid}')
        a = self.merge_sort(arr, start, mid)
        b = self.merge_sort(arr, mid+1, end)
        print(a)
        print(b)
        ans = self.merge(a, b)
        return ans

    def merge(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        i = 0
        j = 0

        m_array = []
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                m_array.append(arr1[i])
                i += 1
            else:
                m_array.append(arr2[j])
                j += 1

        while i < n1:
            m_array.append(arr1[i])
            i += 1

        while j < n2:
            m_array.append(arr2[j])
            j += 1

        return m_array


if __name__ == '__main__':
    a = [6, 5, 4, 3, 2, 1]
    obj = Solution()
    ans = obj.merge_sort(a, 0, len(a)-1)
    print(f'ans is {ans}')
