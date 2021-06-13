class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        print(f'len of arr is {n}')
        hash_map = dict()
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        empty_hash_map = dict()
        for i in A:
            if i not in empty_hash_map:
                empty_hash_map[i] = 1
            else:
                empty_hash_map[i] += 1
        visible = n

        for i in range(len(A) - 1):
            print(f'current_botle: {A[i]}')
            print(empty_hash_map)
            if A[i] < A[i + 1]:
                print(f'bigger bottle {A[i+1]} found for {A[i]}')
                j = i + 1
                count = hash_map[A[i]]
                while count and j < len(A):
                    if empty_hash_map[A[j]] >= count:
                        empty_hash_map[A[j]] -= count
                        visible -= count
                        count = 0
                        break
                    else:
                        count -= empty_hash_map[A[j]]
                        visible -= empty_hash_map[A[j]]
                        empty_hash_map[A[j]] = 0
                        j += 1

                else:
                    pass
            else:
                continue

        return visible

if __name__ == '__main__':
    a = [ 8, 15, 1, 10, 5, 19, 19, 3, 5, 6, 6, 2, 8, 2, 12, 16, 3, 8, 17, 12, 5, 3, 14, 13, 3, 2, 17, 19, 16, 8, 7, 12, 19, 10, 13, 8, 20, 16, 15, 4, 12, 3 ]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is: {ans}')