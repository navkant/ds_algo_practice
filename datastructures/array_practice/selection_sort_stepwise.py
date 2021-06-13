class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        ans = []
        for i in range(len(A)-1):
            min_index = i
            for j in range(i+1, len(A)):
                if A[j] < A[min_index]:
                    min_index = j
            ans.append(min_index)
            A[i], A[min_index] = A[min_index], A[i]
        print(A)
        return ans


if __name__ == "__main__":
    a = [6, 4, 3, 7, 2, 8]
    obj = Solution()
    ans = obj.solve(a)
    print('ans: ', ans)