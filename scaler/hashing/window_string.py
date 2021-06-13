import sys
from collections import Counter


class Solution:
    # @param A : string
    # @param B : string
    # @return a strings

    def minWindow(self, A, B):
        n = len(A)
        k = len(B)
        if n == 1 and k == 1:
            if A != B:
                return ""
            else:
                return A

        dict_b = Counter(B)
        required = len(dict_b)
        window_dict = dict()
        formed = 0

        l = 0
        r = 0
        ans = (float('inf'), 0, 0)

        while r < n:
            char = A[r]
            window_dict[char] = window_dict.get(char, 0) + 1

            if char in dict_b and window_dict[char] == dict_b[char]:
                formed += 1

            while formed == required and l <= r:
                character = A[l]
                if ans[0] > (r - l + 1):
                    ans = (r - l +1, l, r)

                window_dict[character] -= 1

                if character in dict_b and window_dict[character] < dict_b[character]:
                    formed -= 1

                l += 1

            r += 1

        return '' if ans[0] == float('inf') else A[ans[1]: ans[2]+1]


if __name__ == '__main__':
    a = "ADOBECODEBANC"
    b = "ABC"
    obj = Solution()
    ans = obj.minWindow(a, b)
    print(f'ans is {ans}')
