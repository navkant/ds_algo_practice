class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hash_map = dict()
        
        for i in A:
            hash_map[i] = False
        length = 0
        for i in range(len(A)):
            if A[i]-1 in hash_map:
                continue
            else:
                count = 1
                next_element = A[i]
                while True:
                    if next_element + 1 in hash_map:
                        count += 1
                        next_element += 1
                    else:
                        break
                length = max(length, count)
        return length


if __name__ == "__main__":
    a = [ 100, 4, 200, 1, 3, 2 ]
    obj = Solution()
    ans = obj.longestConsecutive(a)
    print('ans is: ', ans)