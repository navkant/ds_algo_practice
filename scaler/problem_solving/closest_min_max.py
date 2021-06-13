import sys

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = {'minn': sys.maxsize, 'maxx': sys.maxsize * -1}
        indices = [0, 0]
        for i in range(len(A)):
            if A[i] < hash_map['minn']:
                hash_map['minn'] = A[i]
                indices[0] = i
            else:
                pass

            if A[i] > hash_map['maxx'] and i > indices[0]:
                hash_map['maxx'] = A[i]
                indices[1] = i

        print(indices)
        return abs(indices[1] - indices[0]) + 1


if __name__ == '__main__':
    a = [814, 761, 697, 483, 981]

    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')