import sys

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        aux_stack = []
        
        sorted_stack = []
        
        while True:
            minn = sys.maxsize
            if len(A) == 0:
                break
            while len(A):
                a = A.pop()
                if a < minn:
                    minn = a
                aux_stack.append(a)
            
            sorted_stack.append(minn)
            print(aux_stack)
            print(minn)
            print(sorted_stack)
            # import pdb;
            # pdb.set_trace()
            added = 1
            while len(aux_stack):
                top = aux_stack.pop()
                if top == minn and added:
                    added = 0
                    continue
                else:
                    A.append(top)
        
        return sorted_stack


if __name__ == "__main__":
    a = [ 66, 96, 43, 28, 14, 1, 41, 76, 70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12 ]
    #  14, 1, 41, 76, 70, 81, 22, 11, 42, 78, 4, 88, 70, 43, 90, 6, 12]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')