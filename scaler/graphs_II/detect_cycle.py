class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def __init__(self):
        self.visit_array = None
        self.adj_list = None
        self.is_cycle = False

    def get_adjacency_list(self, node_count, array):
        adj_list = dict()

        for i in range(1, node_count+1):
            adj_list[i] = list()
        
        for edge in array:
            adj_list[edge[0]].append(edge[1])
        
        return adj_list

    def reset_visit_matrix(self):
        self.visit_array = [False for i in range(len(self.visit_array))]

    def dfs(self, node, prev):
        self.visit_array[node] = True
        nbors = self.adj_list[node]
        print(f'{node} | {nbors}')
        for n in nbors:
            if self.visit_array[n] != True:
                if self.dfs(n, node):
                    return True
            elif self.visit_array[n] == True and n != prev:
                return True
            elif self.visit_array[n] == True and n == prev:
                return True
        self.reset_visit_matrix()
        return False

    def solve(self, A, B):
        self.adj_list = self.get_adjacency_list(A, B)
        self.visit_array = [False for i in range(1, A+2)]
        for k, v in self.adj_list.items():
            print(f'{k} | {v}')
        print()
        for i in range(1, A+1):
            if self.dfs(i, -1):
                print('ans is {}'.format(True))
                return 1
        print('ans is {}'.format(False))
        return 0


if __name__ == '__main__':
    a = 3
    b = [[1, 3],
         [2, 3],
         [3, 2]]
    obj = Solution()
    obj.solve(a, b)