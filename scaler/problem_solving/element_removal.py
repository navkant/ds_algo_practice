class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        print(A)
        n = len(A)
        cost = 0
        for i in range(n):
            sum = 0
            for j in range(n-i):
                sum += A[j]
            print(sum)
            cost += sum
        return cost


if __name__ == '__main__':
    a = [3, 0, 9, 7, 8]
    obj = Solution()
    ans = obj.solve(a)
    print('ans is : ', ans)
