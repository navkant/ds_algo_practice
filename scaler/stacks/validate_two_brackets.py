class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def get_previous_sign(self, string, i):
        if i == 0:
            return True

        if string[i-1] in ('(', '+'):
            return True
        else:
            return False

    def get_sign_array(self, expression):
        n = len(expression)
        stack = [True]
        sign_array = [False] * 26

        for i in range(n):
            if expression[i] in {'-', '+'}:
                continue

            elif expression[i] == '(':
                prev_sign = self.get_previous_sign(expression, i)

                if not prev_sign:
                    stack.append(not stack[-1])
                else:
                    stack.append(stack[-1])
            elif expression[i] == ')':
                stack.pop()
            else:
                prev_sign = self.get_previous_sign(expression, i)
                if stack[-1]:
                    sign_array[ord(expression[i])-97] = prev_sign
                else:
                    sign_array[ord(expression[i]) - 97] = not prev_sign
            print(i, expression[i], prev_sign, stack)
        return sign_array

    def solve(self, A, B):
        s1_array = self.get_sign_array(A)
        print()
        s2_array = self.get_sign_array(B)

        print(s1_array)
        print(s2_array)

        if s1_array == s2_array:
            return 1
        else:
            return 0


if __name__ == "__main__":
    a = "-(a-(-z-(b-(c+t)-x)+l)-q)"
    b = "-a+l-b-(z-(c+t)-x-q)"
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')