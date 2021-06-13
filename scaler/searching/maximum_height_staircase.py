class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        current_height = 1
        while A >= 1:
            if A < current_height:
                break
            else:
                A = A - current_height

            current_height += 1

        return current_height


if __name__ == '__main__':
    a = 10
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
