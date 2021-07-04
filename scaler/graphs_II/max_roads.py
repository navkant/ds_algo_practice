import queue


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def get_adj_list(self, node_count, edge_arr):
        adj_list = dict()
        for i in range(1, node_count+1):
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
        self.visit_matrix = [-1 for i in range(A+1)]
        self.bfs(1, 1)
        print(self.visit_matrix)
        one_count = 0
        zero_count = 0
        for i in self.visit_matrix:
            if i == -1:
                continue
            elif i == 1:
                one_count += 1
            else:
                zero_count += 1
        
        total_edges = one_count * zero_count
        present_edges = A-1
        required_edges = total_edges - present_edges
        print(f'required egdes: {required_edges}')
        return required_edges


if __name__ == '__main__':
    obj = Solution()
    A = 5
    B = [[1, 3],
         [1, 4],
         [3, 2],
         [3, 5]]
    obj.solve(A, B)
