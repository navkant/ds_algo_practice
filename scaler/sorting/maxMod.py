import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        ans = sys.maxsize * -1
        maxx = A[n-1]
        print(A)
        print(maxx)
        for i in range(n):
            mod =  A[i] % maxx
            ans = max(ans, mod)
        
        return ans


if __name__ == "__main__":
    a = [ 927, 707, 374, 394, 279, 799, 878, 937, 431, 112 ]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')