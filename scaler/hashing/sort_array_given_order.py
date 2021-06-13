class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        a_hash = {}
        b_hash = {}
        
        for i in A:
            if i not in a_hash:
                a_hash[i] = 1
            else:
                a_hash[i] += 1
        
        for i in B:
            if i not in b_hash:
                b_hash[i] = 1
            else:
                b_hash[i] += 1

        ans = []
        
        for i in B:
            if i in a_hash and a_hash[i] > 0:
                for k in range(a_hash[i]):
                    ans.append(i)
                    a_hash[i] -= 1
            else:
                pass
        
        A.sort()
        print(a_hash)
        for i in A:
            if a_hash[i] == 0:
                pass
            else:
                ans.append(i)
        
        return ans


if __name__ == "__main__":
    a = [ 10, 2, 18, 16, 16, 16 ]
    b = [ 3, 13, 2, 16, 4, 19 ]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
