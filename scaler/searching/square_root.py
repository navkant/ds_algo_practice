class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        if 4 <= A <= 8:
            return 2

        n = (A // 2)
        start = 1
        end = n
        mid = start + (end - start) // 2

        while start <= end:
            mid = start + (end - start) // 2
            print(f'start {start} mid: {mid} end {end}')
            sqr = mid ** 2
            if sqr == A:
                print('perfect square')
                return mid

            if sqr < A:
                # break
                start = mid + 1
            else:
                end = mid - 1

        if mid ** 2 > A:
            return mid - 1
        return mid


if __name__ == '__main__':
    a = 169
    obj = Solution()
    ans = obj.sqrt(a)
    print(f'ans {ans}')
