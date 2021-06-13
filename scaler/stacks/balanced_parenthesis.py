class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []

        hash_map = {']': '[',
               '}': '{',
               ')': '('}
        
        for i in A:
            print(stack)
            if i in ['(', '[', '{']:
                stack.append(i)
            if i in [')', ']', '}']:
                top = stack.pop()
                if hash_map[i] == top:
                    pass
                else:
                    return 0
        
        print(stack)
        if stack:
            return 0
        else:
            return 1

if __name__ == "__main__":
    a = "{([])}"
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')