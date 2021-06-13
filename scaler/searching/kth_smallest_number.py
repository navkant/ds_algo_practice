class Solution:
    def __init__(self):
        pass

    def count_smaller_equal(self, arr, number):
        n = len(arr)
        count = 0

        for i in range(n):
            if arr[i] <= number:
                count += 1
        return count

    def check_presence(self, arr, element):
        n = len(arr)

        for i in range(n):
            if element == arr[i]:
                return True

        return False

    def solve(self, arr, k):
        n = len(arr)
        minn = arr[0]
        maxx = arr[0]

        for i in range(n):
            minn = min(minn, arr[i])
            maxx = max(maxx, arr[i])

        low = minn
        high = maxx

        while low <= high:
            mid = low + (high - low) // 2

            x1 = self.count_smaller_equal(arr, mid)
            x2 = self.count_smaller_equal(arr, mid-1)
            print(f'low {low} mid {mid} high {high} count {x1}')
            if x1 >= k and x2 < k:
                return mid
            if x1 == k:
                if self.check_presence(arr, mid):
                    return mid
                else:
                    high = mid - 1
                    continue
            if x1 > k:
                high = mid - 1
            else:
                low = mid + 1


if __name__ == '__main__':
    a = [1, 1, 2, 2, 3, 3, 3, 4]
    k = 5
    obj = Solution()
    ans = obj.solve(a, k)
    print(f'ans is {ans}')
