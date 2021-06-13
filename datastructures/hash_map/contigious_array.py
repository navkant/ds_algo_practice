class Solution:
    # @param A : list of integers
    # @return an integer
    hash_map = dict()

    def solve(self, A):
        max_length = 0
        for i in range(len(A)):
            k = i+1
            while k <= len(A):
                sub_array_sum = 0
                subarray_length = 0
                for j in range(i, k):
                    print(A[j], end=' ')
                    sub_array_sum += A[j]
                    subarray_length += 1
                print(f' subarray_sum: {sub_array_sum}  subarray_length: {subarray_length}')
                k += 1
                if sub_array_sum == subarray_length/2:
                    max_length = max(max_length, subarray_length)
            print()
            k += 1
        return max_length

# subarray_set = [] 
# for i in range(len(l)): 
#     k = i+1 
 
#     while k<=len(l): 
#         subarray = [] 
#         for j in range(i,k): 
#             print(l[j], end=' ') 
#             subarray.append(l[j]) 
#         print() 
#         k += 1 
#         subarray_set.append(subarray) 
#     print() 



if __name__ == "__main__":
    a = [ 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0 ]
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)

            
        
        