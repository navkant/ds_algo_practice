class Solution:
	# @param A : list of strings
	# @return an integer
    def __init__(self):
        self.width = None
        self.height = None
        self.adj_mat = None
        self.visit_mat = None
        self.count = 0
    
    def is_in_matrix(self, point):
        if point[0] < 0 or point [1] < 0 or point[0] >= self.height or point[1] >= self.width:
            return False
        else:
            return True
    
    def get_neighbors(self, point):
        adjacent_points = [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]
        neigh_bors = list()

        for n in adjacent_points:
            if self.is_in_matrix(n) and self.adj_mat[n[0]][n[1]] == 'X' and self.visit_mat[n[0]][n[1]]==0:
                neigh_bors.append(n)
        return neigh_bors
    
    def dfs(self, node):
        self.visit_mat[node[0]][node[1]] = 1

        neighs = self.get_neighbors(node)
        print(f'{node} | {neighs}')
        for n in neighs:
            if self.visit_mat[n[0]][n[1]] != 1:
                self.dfs(n)
        

    def black(self, A):
        self.height = len(A)
        self.width = len(A[0])
        self.adj_mat = A

        self.visit_mat = [[0 for j in range(self.width)] for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                if self.visit_mat[i][j] == 0 and self.adj_mat[i][j] == 'X':
                    self.count += 1
                    self.dfs((i, j))
        for row in self.visit_mat:
            print(row)
        print(self.count)
        return self.count


if __name__ == '__main__':
    a = ["X0",
         "0X"]
    obj = Solution()
    obj.black(a)
