from heapq import heappop, heappush

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def __init__(self) -> None:
        self.adj_list = None
        self.first_node = list()

    def get_adjacancy_list(self, node_count, edge_matrix):
        adj_list = {}
        node_list = [0 for i in range(node_count+1)]

        for i in range(1, node_count+1):
            adj_list[i] = list()
        
        for edge in edge_matrix:
            adj_list[edge[0]].append(edge[1])
            node_list[edge[1]] += 1
        
        return adj_list, node_list
    

    def solve(self, A, B):
        self.adj_list, self.indeg = self.get_adjacancy_list(A, B)
        print(self.indeg)
        hp = []
        ans = []

        for i in range(1, A+1):
            if self.indeg[i] == 0:
                heappush(hp, i)
        print(hp)
        while len(hp) != 0:
            xnode = heappop(hp)
            ans.append(xnode)
            nbors = self.adj_list[xnode]
            for n in nbors:
                self.indeg[n] -= 1
                if self.indeg[n] == 0:
                    heappush(hp, n)
        
        if len(ans) != A:
            ans.clear
        print(ans)
        return ans


if __name__ == "__main__":
    a = 6
    b = [[6, 3],
         [6, 1],
         [5, 1],
         [5, 2],
         [3, 4],
         [4, 2]]
    obj = Solution()
    obj.solve(a, b)