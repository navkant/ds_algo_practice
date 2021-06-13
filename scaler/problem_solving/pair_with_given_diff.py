class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        count = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                diff = abs(A[i] - A[j])
                if diff == B:
                    count += 1
        return count


if __name__ == '__main__':
    a = [8, 12, 16, 4, 0, 20]
    print(a)
    obj = Solution()
    ans = obj.solve(a, 4)
    print('ans is: ', ans)
