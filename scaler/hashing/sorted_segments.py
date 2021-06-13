class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def generate_map(self, array, si, ei):
        hash_map = dict()

        for i in range(si, ei + 1):
            if array[i] not in hash_map:
                hash_map[array[i]] = 1
            else:
                hash_map[array[i]] += 1
        return hash_map

    def solve(self, A, B):
        n = len(A)
        ans = list()
        pref_sum = [A[0]]

        for i in range(1, n):
            pref_sum.append(pref_sum[i - 1] + A[i])

        print(pref_sum)

        for q in B:
            start1 = q[0]
            end1 = q[1]
            start2 = q[2]
            end2 = q[3]

            if end2 - start2 != end1 - start1:
                ans.append(0)
                continue

            if start1 != 0:
                sum1 = pref_sum[end1] - pref_sum[start1-1]
            else:
                sum1 = pref_sum[end1]

            if start2 != 0:
                sum2 = pref_sum[end2] - pref_sum[start2-1]
            else:
                sum2 = pref_sum[end2]

            if sum1 == sum2:
                x = self.generate_map(A, q[0], q[1])
                y = self.generate_map(A, q[2], q[3])

                if x == y:
                    ans.append(1)
                else:
                    ans.append(0)
            else:
                ans.append(0)

        return ans


if __name__ == '__main__':
    a = [1, 7, 11, 8, 11, 7, 1]
    b = [[0, 2, 4, 6]]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
