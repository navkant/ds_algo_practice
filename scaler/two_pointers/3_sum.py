import sys

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        A.sort()
        print(A)
        for i in range(n):
            print((i, A[i]), end=' ')
        print()
        i = 0
        j = n - 1

        if len(A) == 3 and sum(A) <= B:
            return sum(A)

        ans = sys.maxsize * -1
        while i < j:
            summ = A[i] + A[j]
            print(f'i {i} j {j} summ {summ}, ans {ans}')
            if summ >= B:
                if summ == B:
                    for k in range(i+1, j):
                        if A[k] == 0:
                            ans = summ
                        else:
                            continue
                j -= 1

            elif A[i] + A[j] < B:
                print('lesser found')
                summ = A[i] + A[j]
                flag = False
                for k in range(i+1, j):
                    print('checking third element ', A[k], summ + A[k])
                    if summ + A[k] >= B:
                        if summ + A[k] == B:
                            summ += A[k]
                            print('ans found ', summ)
                            flag = True
                            ans = summ
                        break
                    else:
                        continue
                
                if flag:
                    pass
                else:
                    summ += A[k]
                    if abs(summ - B) < abs (ans - B):
                        ans = summ

                i += 1

        return ans


if __name__ == '__main__':
    a = [ 4, -3, 4, -4, -3, 1, -6, -7, -3, -8, 10 ]
    b = -5
    obj = Solution()
    ans = obj.threeSumClosest(a, b)
    print(f'ans is {ans}')


