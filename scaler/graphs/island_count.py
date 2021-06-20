class Solution:
    # @param A : list of list of integers
    # @return an integer
    def __init__(self):
        self.count = 0

    def is_in_matrix(self, point, width, height):
        if point[0] < 0 or point[1] < 0 or point[0] > height or point[1] > width:
            return False
        else:
            return True

    def get_neighbours(self, point):
        neigh = [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1]),
                 (point[0]-1, point[1]+1), (point[0]+1, point[1]+1), (point[0]+1, point[1]-1), (point[0]-1, point[1]-1)]
        # print(f'{point} | {neigh}')
        return neigh

    def dfs(self, root, adj_mat, visit_mat, width, height):
        if adj_mat[root[0]][root[1]] == 0 or visit_mat[root[0]][root[1]] == 1:
            visit_mat[root[0]][root[1]] = 1
            return

        visit_mat[root[0]][root[1]] = 1
        neighbours = self.get_neighbours(root)
        valid_nbrs = []
        for n in neighbours:
            if self.is_in_matrix(n, width, height) and visit_mat[n[0]][n[1]] != 1 and adj_mat[n[0]][n[1]]:
                valid_nbrs.append(n)
        
        print(f'point: {root} | {valid_nbrs}')

        for neb in valid_nbrs:
            self.dfs(neb, adj_mat, visit_mat, width, height)
            # self.count += 1

    def solve(self, A):
        height = len(A)
        width = len(A[0])
        v_mat = [[0 for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                if v_mat[i][j] == 0 and A[i][j] == 1:
                    self.count += 1
                self.dfs((i, j), A, v_mat, width-1, height-1)
                print(f'({i},{j}) | {self.count}')
        for row in v_mat:
            print(row)
        ans = self.count
        print(f'ans is {ans}')


if __name__ == '__main__':
    a = [[1, 1, 0, 0, 1],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
    obj = Solution()
    obj.solve(a)
