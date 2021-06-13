class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def get_gcd(self, A, B):
        if A == 0 or B == 0:
            return max(A, B)

        if A > B:
            return self.get_gcd(B, A % B)
        else:
            return self.get_gcd(A, B % A)


    def getFinal(self, A, B):
        if A == 0:
            return B
        elif B == 0:
            return A

        if A > B:
            if A % B == 0:
                return 2 * B
            else:
                while True:
                    print(f'A {A} B {B}')
                    if B == 0:
                        break
                    temp = B
                    B = A % B
                    A = temp
                return A
        else:
            if B % A == 0:
                return 2 * A
            else:
                while True:
                    if A == 0:
                        break
                    temp = B
                    A = B % A
                    B = temp
                return B


if __name__ == '__main__':
    a = 11
    b = 4
    obj = Solution()
    ans = obj.getFinal(a, b)
    print(f'ans is {ans}')
