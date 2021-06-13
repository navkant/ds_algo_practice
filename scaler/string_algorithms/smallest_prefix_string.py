class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def smallestPrefix(self, A, B):
        m = len(A)
        n = len(B)
        i = 0
        j = 0
        ans = ""

        for i in A:
            if ord(i) <= ord(B[0]):
                ans = ans + i
            else:
                ans = A
                break

        ans = ans + B[0]

        # for i in range(n):
        #     if ans and B[i] >= ans[-1]:
        #         ans += B[i]
        #     else:
        #         break

        return ans


if __name__ == '__main__':
    a = 'ertuyivhfg'
    b = 'v'
    obj = Solution()
    ans = obj.smallestPrefix(a, b)
    print(f'ans is {ans}')