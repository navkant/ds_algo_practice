class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = dict()
        
        for i in range(1, len(A)):
            curr_sum = A[i] + A[i-1]
            A[i] = curr_sum
            print(curr_sum)
            if curr_sum == 0:
                return 1
            elif curr_sum in hash_map:
                return 1
            elif curr_sum not in hash_map:
                hash_map[curr_sum] = i
        return 0


if __name__ == "__main__":
    a = [ 5, 17, -22, 11 ]
    obj = Solution()
    ans = obj.solve(a)
    print(ans)