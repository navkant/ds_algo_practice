class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        B = sorted(A)
        n = len(A)
        indices = []
        for i in range(n):
            if A[i] != B[i]:
                indices.append(i)
            else:
                continue
        if indices:
            return indices[-1] - indices[0]
        else:
            return 0


if __name__ == '__main__':
    a = [-355071087, -679308132, 398052175, 755454983, 814022370, 889267058]
    obj = Solution()
    ans = obj.solve(a)
    print('ans is: ', ans)
