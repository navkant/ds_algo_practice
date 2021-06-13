class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        hash_map = dict()

        ans = 99999999999
        for i in range(n):
            if A[i] not in hash_map:
                hash_map[A[i]] = i
            else:
                ans = min(ans, i - hash_map[A[i]])

        return ans


if __name__ == '__main__':
    a = [7, 1, 3, 4, 1, 7]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
