class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        maxx = A[0]

        for i in A:
            maxx = max(i, maxx)
        print(maxx)
        hash_map = {0: 1, 1: 1}

        for i in range(2, maxx+1):
            hash_map[i] = 1

        for i in range(2, maxx + 1):
            element = i
            while element <= maxx:
                print(element, end=' ')
                hash_map[element] += 1
                element += i
            print()
        print(hash_map)
        ans = []
        for i in A:
            ans.append(hash_map[i])

        return ans


if __name__ == '__main__':
    a = [10, 20]
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
    # 1, 10, 2, 5
    # 1, 20, 2, 10,