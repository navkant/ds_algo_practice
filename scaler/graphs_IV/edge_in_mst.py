from heapq import heappop, heappush

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        hp = list()
        for edge in B:
            heappush(hp, (edge[2], (edge[0], edge[1])))

        while hp:
            weight, node = heappop(hp)
            


if __name__ == '__main__':
    A = 3
    B = [[1, 2, 2],
         [1, 3, 2],
         [2, 3, 3]]
    obj = Solution()
    obj.solve(A, B)
