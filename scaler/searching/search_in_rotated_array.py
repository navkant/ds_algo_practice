class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer

    def search(self, A, B):
        if len(A) == 1 and A[0] == B:
            return 0
        if len(A) == 1 and A[0] != B:
            return -1
        n = len(A)

        start = 0
        end = n - 1
        # [1, 7, 67, 133, 178]

        pivot = 0
        while start <= end:
            mid = start + (end - start) // 2
            print(f'mid {mid}')

            if A[mid] > A[mid + 1]:
                pivot = mid
                break
            elif A[mid] < A[mid - 1]:
                pivot = mid - 1
                break
            elif A[mid] < A[start]:
                end = mid - 1
            elif A[end] < A[mid]:
                start = mid + 1
            else:
                break
        # print(f'pivot: {pivot}')

        if B == A[pivot]:
            return pivot

        if pivot != 0:
            if B >= A[0]:
                start = 0
                end = pivot
                count = 0
                while start <= end:
                    mid = start + (end - start) // 2
                    # print(f' start: {start} mid: {mid} end: {end}')

                    if A[mid] == B:
                        return mid
                    elif A[mid] > B:
                        end = mid - 1
                    else:
                        start = mid + 1
                    count += 1
            else:
                start = pivot + 1
                end = n - 1
                count = 0
                while start <= end:
                    mid = start + (end - start) // 2
                    # print(f' start: {start} mid: {mid} end: {end}')

                    if A[mid] == B:
                        return mid
                    elif A[mid] > B:
                        end = mid - 1
                    else:
                        start = mid + 1
                    count += 1
        else:
            start = 0
            end = n-1
            while start <= end:
                mid = start + (end - start) // 2
                if A[mid] == B:
                    return mid
                elif A[mid] > B:
                    end = mid - 1
                else:
                    start = mid + 1

        return -1



if __name__ == '__main__':
    a = [1, 2, 3, 4, 5 ]
    b = 3
    obj = Solution()
    ans = obj.search(a, b)
    print(f'ans is {ans}')
