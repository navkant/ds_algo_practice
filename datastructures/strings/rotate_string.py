class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings

    def reverse_string(self, string):
        rev_string = ''

        for i in range(len(string)-1, -1, -1):
            rev_string += string[i]
        return rev_string
    
    def split_string(self, string, point):
        first_string = ''
        second_string = ''
        
        for i in range(len(string)):
            if i < point:
                first_string += string[i]
            else:
                second_string += string[i]
        return (first_string, second_string)

    def solve(self, A, B):
        if B > len(A):
            B = B % len(A)
        rev_string = self.reverse_string(A)
        f_string, s_string = self.split_string(rev_string, B)

        rev_f_string = self.reverse_string(f_string)
        rev_s_string = self.reverse_string(s_string)

        return rev_f_string + rev_s_string


if __name__ == "__main__":
    a = 'nrsizekitrkpbkqxsmq'
    obj = Solution()
    ans = obj.solve(a, 56)
    print('ans is: ', ans)