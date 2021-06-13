class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        
        for i in range(1, len(A)-1, 2):
            A[i], A[i+1] = A[i+1], A[i]
        
        return A
            
if __name__ == "__main__":
    a = [1, 2, 3, 4]
    obj = Solution()
    ans = obj.wave(a)
    print('ans is: ', ans)