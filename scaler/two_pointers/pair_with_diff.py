class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        print(A)
        n = len(A)
        # print(A)
        hash_map = {}

        count = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if A[j] - A[i] == B:
                    tupple = (A[i], A[j])
                    if tupple not in hash_map:
                        hash_map[tupple] = 1
                        count += 1
                    else:
                        pass

                elif A[i] - A[j] > B:
                    break

        return count


if __name__ == "__main__":
    a = [8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3]
    b = 3
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
