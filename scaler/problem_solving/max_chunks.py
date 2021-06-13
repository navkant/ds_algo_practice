class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        B = sorted(A)
        hash_map = dict()
        unequals = set()
        ans = 0

        for i in range(n):
            if A[i] in hash_map:
                hash_map[A[i]] += 1
                if hash_map[A[i]] == 0:
                    unequals.remove(A[i])
                else:
                    unequals.add(A[i])
            else:
                hash_map[A[i]] = 1
                unequals.add(A[i])

            if B[i] in hash_map:
                hash_map[B[i]] -= 1
                if hash_map[B[i]] == 0:
                    unequals.remove(B[i])
                else:
                    unequals.add(B[i])
            else:
                hash_map[B[i]] = -1
                unequals.add(B[i])
            print(unequals)
            if len(unequals) == 0:
                ans += 1

        return ans


if __name__ == '__main__':
    a = [3, 2, 3, 4, 0]
    #   [0, 2, 3, 3, 4]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
