class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def __init__(self):
        pass

    def rec_func(self, A, output, ans):
        if len(A) == 0:
            if output not in ans:
                ans.append(output)
            return

        for i in range(len(A)):
            first_element = A[i]
            B = []
            for j in range(i):
                B.append(A[j])
            for j in range(i+1, len(A)):
                B.append(A[j])

            # print(f'A : {A} B: {B} output: {output}')
            self.rec_func(B, output + [first_element], ans)

    def permute(self, A):
        n = len(A)
        ans = []
        self.rec_func(A, [], ans)
        return ans


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7, 8 ]
    obj = Solution()
    ans = obj.permute(a)
    print(f'ans is {ans}')
