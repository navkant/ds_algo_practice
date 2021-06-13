class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        number = 0
        N = len(A)
        for i in range(N-1, -1, -1):
            print('i: ', i)
            n = ord(A[i]) - 64
            value = n * (26**(N-i-1))
            print('value: ', value)
            number += value

        return number


if __name__ == '__main__':
    a = 'AB'
    obj = Solution()
    ans =  obj.titleToNumber(a)
    print('ans is :', ans)
