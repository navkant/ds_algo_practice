class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        l = 0
        r = 0
        
        summ = A[0]

        while l < n and r < n:
            print(f'l: {l} r: {r} summ: {summ}')
            if l == n - 1 and r == n - 1:
                if summ == B:
                    return A[l:r+1]
                else:
                    break

            if summ < B:
                if r == n - 1 and summ < B:
                    break
                else:
                    r += 1
                    summ += A[r]
            
            if summ == B:
                print('************')
                return A[l:r+1]
            
            if summ > B:
                summ -= A[l]
                l += 1
        
        return [-1]


if __name__ == "__main__":
    a = [1, 1000000000]
    b = 1000000000
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
