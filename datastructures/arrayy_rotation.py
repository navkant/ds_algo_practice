class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    
    def reverse_arr(self, A, start, end):
        n = start + ((end - start)//2)
        for i in range(start, n+1):
            last = end - i + start
            A[i], A[last] = A[last], A[i]
        return A
    
    def rotate_array(self, arr, k):
        k = len(arr) - k
        # reversing whole array
        arr = self.reverse_arr(arr, 0, len(arr)-1);
        # reversing first subarray
        arr = self.reverse_arr(arr, 0, k-1);
        # reversing second subarray
        arr = self.reverse_arr(arr, k, len(arr)-1);
        return arr;

    def solve(self, A, B):
        result = list()
        
        for i in B:
            if i > len(A):
                i = i % len(A)
            else:
                pass
            temp_arr = self.rotate_array(A, i)
            
            result.append(temp_arr)
        return result

    def solve(self, A, B):
        result = list()
        
        for i in B:
            if i > len(A):
                i = i % len(A)
            else:
                pass
            temp_arr = self.rotate_array(A, i)
            print(temp_arr)
            c = temp_arr.copy()
            result.append(c)
        return result


if __name__ == "__main__":
    x = [ 1, 2, 3, 4, 5 ]
    print(x)
    y = [2, 3]
    obj = Solution()
    ans = obj.solve(x, y)
    print(ans)
