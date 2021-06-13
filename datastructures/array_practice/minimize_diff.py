class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        maxx = 0
        k = B
        for i in range(len(A)):
            maxx = max(maxx, A[i])
        
        freq = [0] * (maxx+1)
        for i in range(len(A)):
            freq[A[i]] = freq[A[i]] + 1
        
        i = 0
        j = maxx
        while (i<j):
            if freq[i] > freq[j]:
                if freq[j] <= k:
                    freq[j-1] = freq[j-1] + freq[j]
                    k = k - freq[j]
                    j = j - 1
                else:
                    break
            else:
                if freq[i] <= k:
                    freq[i+1] = freq[i+1] + freq[i]
                    k = k - freq[i]
                    i = i + 1
                else:
                    break
        return j-i
                

if __name__ == "__main__":
    a = [2, 6, 3, 9, 8]
    # print(a)
    b = 3
    obj = Solution()
    ans = obj.solve(a, b)
    print('ans is: ', ans)