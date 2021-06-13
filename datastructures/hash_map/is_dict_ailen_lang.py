class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        if len(A) == 1:
            return 1

        for i in range(len(A)-1):
            first_word = A[i]
            second_word = A[i+1]
            j = 0
            flag = 0
            while j < min(len(first_word), len(second_word)):
                if first_word[j] != second_word[j]:
                    if B.index(first_word[j]) > B.index(second_word[j]):
                        return 0
                    break
                j += 1
            if flag == 0:
                if len(first_word) > (len(second_word)):
                    return 0
        return 1


if __name__ == "__main__":
    A = [ "hello", "scaler", "interviewbit" ]
    B = "adhbcfegskjlponmirqtxwuvzy"
    print(B)
    obj = Solution()
    ans = obj.solve(A, B)
    print("ans is: ", ans)
