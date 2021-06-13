class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        print(A)
        n = len(A)
        j = n - 1
        same_cont = 0

        count = 0
        hash_map = {}
        # for k in range(n):
        #     if A[k] ** 2 < B:
        #         print(A[k] ** 2)
        #         count += 1
        #     else:
        #         break
        # print(count)

        for i in range(n):
            while j >= i and (A[i] * A[j]) >= B:
                j = j - 1
            if i <= j:
                count += (j - i + 1) * 2
                same_cont += 1

        return count - same_cont

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    b = 5
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')