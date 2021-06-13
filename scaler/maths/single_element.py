class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(32):
            count = 0
            for j in range(len(A)):
                if (A[j] >> i) & 1:
                    count += 1

            if count % 3 != 0:
                ans = ans | (1 << i)

        return ans


if __name__ == '__main__':
    a = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]
    obj = Solution()
    ans = obj.singleNumber(a)
    print(f'ans is {ans}')


