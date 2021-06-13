import sys


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        odd_chars = ""
        even_chars = ""

        for i in range(n):
            if ord(A[i]) % 2 == 0:
                odd_chars = odd_chars + A[i]
            else:
                even_chars = even_chars + A[i]

        odd_max = sys.maxsize * -1
        odd_min = sys.maxsize
        even_max = sys.maxsize * -1
        even_min = sys.maxsize

        for i in range(len(odd_chars)):
            odd_max = max(odd_max, ord(odd_chars[i]))
            odd_min = min(odd_min, ord(odd_chars[i]))

        for i in range(len(even_chars)):
            even_max = max(even_max, ord(even_chars[i]))
            even_min = min(even_min, ord(even_chars[i]))

        if abs(odd_max - even_min) != 1 or abs(odd_min - even_max) != 1:
            return True
        else:
            return False


if __name__ == '__main__':
    a = "aab"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
