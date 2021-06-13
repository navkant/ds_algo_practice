class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        ans = []
        for i in range(n):
            size = A[i]
            sieve = [1] * (size + 1)

            for j in range(2, len(sieve)):
                for k in range(j, len(sieve), j):
                    sieve[k] += 1
            ans.append(sieve[-1])

        return ans


if __name__ == '__main__':
    a = [8, 9, 10]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')