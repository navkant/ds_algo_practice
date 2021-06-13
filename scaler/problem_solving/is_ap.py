class Solution:
    # @param A : list of integers
    # @return an integer

    def two_minimum(self, array):
        min1 = 10 ** 7
        min2 = 10 ** 7
        n = len(array)
        for i in range(n):
            if array[i] < min1:
                min1 = array[i]

        for i in range(n):
            if array[i] == min1:
                continue
            else:
                if array[i] < min2:
                    min2 = array[i]
        # print(f'min1: {min1} min2: {min2}')
        return (min1, min2)

    def find_common_diff(self, min1, min2):
        return min2 - min1

    def solve(self, A):
        first, second = self.two_minimum(A)
        cd = self.find_common_diff(first, second)
        print('cd: ', cd)
        n = len(A)
        for i in range(1, n):
            if abs(A[i] - A[i - 1]) % cd == 0:
                continue
            else:
                return 0
        return 1


if __name__ == '__main__':
    a = [3,5,1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is : {ans}')