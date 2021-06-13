class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        ans = [0] * A

        for i in range(0, A):
            ans[i] = 1000000000

        for a in range(1, 51):
            for d in range(1, 51):
                temp = [0] * A
                # print(temp)
                for i in range(0, A):
                    temp[i] = a + i * d

                fB = False
                fC = False
                for i in range(0, A):
                    if temp[i] == B:
                        fB = True
                    elif temp[i] == C:
                        fC = True

                if fB is True and fC is True and temp[A-1] < ans[A-1]:
                    for i in range(0, A):
                        ans[i] = temp[i]

        return ans


if __name__ == '__main__':
    a = 5
    b = 17
    c = 32
    obj = Solution()
    ans = obj.solve(a, b, c)
    print('ans is: ', ans)
