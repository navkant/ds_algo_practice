class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        print(A)
        for i in range(len(A)):
            if i == len(A)-1 and A[i]==0:
                return 1
            else:
                pass
            if A[i] == (len(A)-i-1) and A[i] != A[i+1]:
                return 1
            else:
                continue
        return -1   

if __name__ == "__main__":
    a = [ 4, -9, 8, 5, -1, 7, 5, 3 ]
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)