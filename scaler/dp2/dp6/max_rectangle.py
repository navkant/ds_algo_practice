class KadanesAlgo:
    def get_maximum_sum(self, array):
        max_ending_here = max_so_far = 0
        for i in range(len(array)):
            max_ending_here = max_ending_here + array[i]
            if max_ending_here < 0:
                max_ending_here = 0
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            else:
                pass
        return max_so_far

    def solve(self, a):
        ans = self.get_maximum_sum(a)
        return ans


class Solution:
    def get_max_rectangle(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        ans = float('-inf')

        curr_arr = [0 for i in range(m)]
        for j1 in range(n):
            for j2 in range(j1, n):
                curr_arr = [curr_arr[i] + matrix[i][j2] for i in range(m)]
                print(curr_arr)
                obj = KadanesAlgo()
                max_till_here = obj.solve(curr_arr)
                ans = max(max_till_here, ans)
            print()
            curr_arr = [0 for i in range(m)]

        return ans

    def solve(self, matrix):
        ans = self.get_max_rectangle(matrix)
        print(f'ans is {ans}')



if __name__ == '__main__':
    mat = [[1, 3, -2],
         [1, 4, 6],
         [-4, -2, 1]]
    obj = Solution()
    obj.solve(mat)
