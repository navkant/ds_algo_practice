class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        pref_sum = [A[0]]

        for i in range(1, n):
            pref_sum.append(pref_sum[i - 1] + A[i])
        print(pref_sum)
        hash_map = dict()

        for i in range(n):
            if i != 0 and pref_sum[i] == 0:
                return 1
            elif pref_sum[i] not in hash_map:
                hash_map[pref_sum[i]] = 1
            elif A[i] in hash_map:
                return 1

        return 0

if __name__ == '__main__':
    a = [-1, 1]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')