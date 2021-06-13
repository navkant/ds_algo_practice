class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = dict()

        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        n = len(A)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                sum = A[i] + A[j]
                if sum in hash_map:
                    count += 1
                else:
                    continue
        return count


if __name__ == '__main__':
    a = [ 3, 4, 2, 6 ,7]
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is : ', ans)