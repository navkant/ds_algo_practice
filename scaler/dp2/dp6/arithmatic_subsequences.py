class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.count = 0
        self.hash = {}

    def is_subsequence_recursive(self, A, i, subsequence):
        if i == len(A):
            if len(subsequence) >= 3:
                if tuple(subsequence) not in self.hash:
                    print(subsequence)
                    self.count += 1
                    self.hash[tuple(subsequence)] = 1
                return
            else:
                return

        if len(subsequence) >= 3 and tuple(subsequence) not in self.hash:
            print(subsequence)
            self.count += 1
            self.hash[tuple(subsequence)] = 1

        if len(subsequence) < 2:
            n_ss = subsequence.copy()
            n_ss.append(A[i])
            self.is_subsequence_recursive(A, i+1, subsequence)
            self.is_subsequence_recursive(A, i+1, n_ss)
        else:
            if A[i] - subsequence[-1] == subsequence[-1] - subsequence[-2]:
                nn_ss = subsequence.copy()
                nn_ss.append(A[i])
                self.is_subsequence_recursive(A, i+1, nn_ss)
                self.is_subsequence_recursive(A, i+1, subsequence)
            else:
                self.is_subsequence_recursive(A, i+1, subsequence)

    def solve(self, A):
        s = list()
        ans = self.is_subsequence_recursive(A, 0, s)
        print(f'ans is {ans}')
        print(f'ans is {self.count}')


if __name__ == '__main__':
    a = [-2, -4, -10, 10, 7, 3, 6, -3, -4, -6]
    obj = Solution()
    obj.solve(a)
