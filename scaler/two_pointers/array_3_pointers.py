import sys

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        m = len(A)
        n = len(B)
        o = len(C)
        i = 0
        j = 0
        k = 0
        
        ans = sys.maxsize

        while i < m and j < n and k < o:
            minn = min(A[i], B[j], C[k])
            maxx = max(A[i], B[j], C[k])
            diff = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
            
            ans = min(ans, diff)
            
            if minn == A[i]:
                i += 1
            elif minn == B[j]:
                j += 1
            elif minn == C[j]:
                k += 1
        
        return ans


if __name__ == "__main__":
    a = [3, 5, 6]
    b = [2]
    c = [3, 4]
    obj = Solution()
    ans = obj.minimize(a, b, c)
    print(f'ans is {ans}')
