class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers

    def solve(self, A, B):
        new_array = A.copy()
        for i in range(1, len(A)):
            curr_sum = A[i] + A[i-1]
            A[i] = curr_sum

        hash_map = dict()
        for i in range(len(A)):
            if (A[i] - B in hash_map) or (A[i] + B in hash_map):
                sub_array = list()
                if A[i] - B in hash_map:
                    for x in range(hash_map[A[i]-B]+1, i+1):
                        sub_array.append(new_array[x])
                    return sub_array
                else:
                    for x in range(hash_map[A[i]+B]+1, i+1):
                        sub_array.append(new_array[x])
                    return sub_array
            else:
                hash_map[A[i]] = i
        return -1


if __name__ == "__main__":
    a = [ 15, 2, 48, 19, 28, 22, 44, 2, 32, 46, 46, 24, 1, 23, 49, 26, 23, 17, 17, 46, 4, 30, 40, 36, 20, 5 ]
    print(a)
    b = 82
    obj = Solution()
    ans = obj.solve(a, b)
    print(ans)
        
