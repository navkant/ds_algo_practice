import queue

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def __init__(self):
        pass


    def get_adj_list(self, node_count, edge_arr):
        adj_list = dict()
        for i in range(node_count):
            adj_list[i] = list()
        
        for edge in edge_arr:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        
        for k, v in adj_list.items():
            print(f'{k} | {v}')
        print()
        return adj_list

    def bfs(self, node, color):
        if self.visit_matrix[node] != -1:
            return True
        q = queue.Queue()
        q.put(node)
        self.visit_matrix[node] = color

        while not q.empty():
            xnode = q.get()
            nbors = self.adj_list[xnode]
            print(f"{xnode} | {nbors}")
            new_color = int(not self.visit_matrix[xnode])

            for n in nbors:
                if self.visit_matrix[n] != -1 and self.visit_matrix[n] == self.visit_matrix[xnode]: # and n != xnode:
                    return False
                elif self.visit_matrix[n] != -1 and self.visit_matrix[n] != self.visit_matrix[xnode]: # and n != xnode:
                    continue
                elif self.visit_matrix[n] == -1: # and n != xnode:
                    q.put(n)
                    print(f"     nbor: {n}")
                    self.visit_matrix[n] = new_color
        return True

    def solve(self, A, B):
        self.adj_list = self.get_adj_list(A, B)
        
        self.visit_matrix = [-1 for i in range(A)]

        for i in range(A):
            ans = self.bfs(i, 1)
            if not ans:
                print(f'graph is not bipartide')
                return 0
        
        print(self.visit_matrix)

        print('graph is bipartide')
        return 1



if __name__ == '__main__':
    a = 10
    b = [[7, 8],[1, 2], [0, 9], [1, 3], [6, 7], [0, 3], [2, 5], [3, 8], [4, 8]]
    obj = Solution()
    obj.solve(a, b)
