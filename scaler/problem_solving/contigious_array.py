class Solution:
    # @param A : list of integers
    # @return an integer
    hash_map = dict()

    def solve(self, A):
        for i in range(len(A)):
            if A[i] == 0:
                A[i] = -1
            else:
                continue
        print(A)
        for i in range(1, len(A)):
            curr_sum = A[i] + A[i - 1]
            A[i] = curr_sum

        hash_map = dict()
        print(A)
        max_length = 0
        for i in range(len(A)):
            print(hash_map, max_length, end=' ')
            if A[i] == 0:
                max_length = max(max_length, i + 1)
            if A[i] not in hash_map:
                hash_map[A[i]] = i
            else:
                prev_index = hash_map[A[i]]
                print(A[i])
                max_length = max(max_length, i - prev_index)
            print( )
        return max_length


if __name__ == "__main__":
    a = [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
