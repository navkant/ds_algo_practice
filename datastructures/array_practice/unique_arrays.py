class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # sort the array
        A.sort()
    
        # initialize variables
    
        steps = 0
        i = 1
        j = 0
        
        # loop unitil you reach the end
        while j < n:
            
            # make current element unique
            if i >= A[j]: 
                steps += (i - A[j])
                j += 1
                i+=1
            else:
                i = A[j] + 1
                j += 1
            print(f'steps: {steps}')
        # return the answer
        return steps

if __name__ == "__main__":
    a = [3, 3, 4]
    obj = Solution()
    ans = obj.solve(a)
    print('ans is', ans)