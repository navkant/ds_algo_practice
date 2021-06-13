class Solution:
    # @param A : string
    # @return a strings

    def reverse_string(self, string):
        n = len(string)
        ans = ""

        for i in range(n-1, -1, -1):
            ans = ans + string[i]

        return ans

    def remove_extra_spaces(self, string):
        print(string, '.')
        n = len(string)
        ans = ""

        for i in range(n):
            print(string[i])
            if i == n - 1 and string[i] == ' ':
                continue
            if ans and ans[-1] == ' ' and string[i] == ' ':
                continue
            elif not ans and string[i] == ' ':
                continue
            else:
                ans = ans + string[i]

        return ans

    def solve(self, A):
        # A = self.remove_extra_spaces(A)
        rev_sentence = A[::-1]
        rev_sentence = rev_sentence.split(' ')

        for i in range(len(rev_sentence)):
            rev_sentence[i] = self.reverse_string(rev_sentence[i])
        print(rev_sentence)
        ans = []

        for w in rev_sentence:
            if w == '':
                continue
            else:
                ans.append(w)
        print(ans)

        return ' '.join(ans)


if __name__ == '__main__':
    a = " this string hello  "
    obj = Solution()
    ans = obj.solve(a)
    print(f"ans is {ans}")



