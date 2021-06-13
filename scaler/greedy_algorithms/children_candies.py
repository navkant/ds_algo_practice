class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        n = len(A)
        cl = [1]
        cr = [1]

        for i in range(1, n):
            if A[i] > A[i-1]:
                cl.append(cl[i-1]+1)
            else:
                cl.append(1)
        print(f'cl: {cl}')
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                cr.append(cr[n - i - 2] + 1)
            else:
                cr.append(1)

        cr = cr[::-1]
        print(f'cr: {cr}')
        for i in range(n):
            cl[i] = max(cl[i], cr[i])
        print(f'cl: {cl}')
        return sum(cl)


if __name__ == '__main__':
    a = [1, 6, 10, 8, 7, 3, 2]
    obj = Solution()
    print(f'aa: {a}')
    ans = obj.candy(a)
    print(f'ans is {ans}')