class Solution:
    # @param A : string
    # @return an integer
    def LBSlength(self, A):
        n = len(A)
        ans = 0
        s = []
        curr = 0
        dct = {')': '(', '>': '<', ']': '[', '}': '{'}

        for i in A:
            if i in list(dct.values()):
                s.append((i, curr))
                curr = 0
            else:
                if len(s) > 0 and dct[i] == s[-1][0]:
                    curr += 2 + s[-1][1]
                    s.pop()
                else:
                    s = []
                    curr = 0

                ans = max(ans, curr)
        print(s, curr)
        while len(s):
            ans = max(ans, s[-1][1])
            s.pop()

        return ans


if __name__ == '__main__':
    s = "5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190"
    a = "[]]"
    obj = Solution()
    ans = obj.LBSlength(a)
    print(f'ans is {ans}')