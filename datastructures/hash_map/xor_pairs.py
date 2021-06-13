class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        hash_map = {}
        count = 0
        for i in A:
            if B ^ i not in hash_map:
                hash_map[i] = 1
            else:
                count += 1
        return count


if __name__ == "__main__":
    a = [3, 6, 8, 10, 15, 50]
    target = 5
    obj = Solution()
    ans = obj.solve(a, target)
    print(ans)