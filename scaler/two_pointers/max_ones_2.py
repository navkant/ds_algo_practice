class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        n = len(A)
        i = 0
        j = 0
        zero_count = 0
        if A[i] == 0:
            zero_count += 1
        ans_i = 0
        ans_j = 0

        while j < n:
            if zero_count <= B:
                j += 1
                if j < n and A[j] == 0:
                    zero_count += 1

            if zero_count > B:
                if A[i] == 0:
                    zero_count -= 1
                i += 1

            if j >= n:
                if n - i - 1 > ans_j - ans_i:
                    ans_j = n - 1
                    ans_i = i
            elif j - i > ans_j - ans_i:
                ans_j = j
                ans_i = i

        return list([x for x in range(ans_i, ans_j+1)])


if __name__ == '__main__':
    a = [1, 1, 0, 0, 1, 1, 1, 0, 0, 0]  # , 0, 0, 0, 0]  # ], 1, 1, 1, 1, 0 ]
    b = 4
    obj = Solution()
    ans = obj.maxone(a, b)
    print(f'ans is {ans}')
