import queue

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def __init__(self):
        self.width = None
        self.height = None
        self.adj_mat = None
        self.visit_mat = None
        self.dist_mat = None
        self.all_ones = list()
    
    def is_in_matrix(self, point):
        if point[0] < 0 or point[1] < 0 or point[0] >= self.height or point[1] >= self.width:
            return False
        else:
            return True
    
    def get_valid_neighbours(self, point):
        if point == (-1, -1):
            return self.all_ones

        neigh = [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]
        # print(f'{point} | {neigh}')
        valid_nbors = list()

        for n in neigh:
            if self.is_in_matrix(n) and self.visit_mat[n[0]][n[1]] != 1:
                valid_nbors.append(n)
        return valid_nbors

    def bfs(self, node):
        if node == (-1, -1):
            pass
        else:
            self.visit_mat[node[0]][node[1]] = 1

        q = queue.Queue()
        q.put((node, -1))

        while not q.empty():
            new_node = q.get()
            nebors = self.get_valid_neighbours(new_node[0])
            for nb in nebors:
                x = (nb, new_node[1]+1)
                q.put(x)
                self.visit_mat[nb[0]][nb[1]] = 1
                self.dist_mat[nb[0]][nb[1]] = min(new_node[1]+1, self.dist_mat[nb[0]][nb[1]])

    def solve(self, A):
        self.height = len(A)
        self.width = len(A[0])
        self.adj_mat = A
        self.visit_mat = [[0 for j in range(self.width)] for i in range(self.height)]
        self.dist_mat = [[float('inf') for j in range(self.width)] for i in range(self.height)]

        root = (-1, -1)

        for i in range(self.height):
            for j in range(self.width):
                if A[i][j] == 1:
                    self.all_ones.append((i, j))

        self.bfs(root)        

        for row in self.dist_mat:
            print(row)
        
        return self.dist_mat


if __name__ == "__main__":
    a = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 0]]
    obj = Solution()
    obj.solve(a)
