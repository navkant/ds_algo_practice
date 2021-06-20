import queue

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def __init__(self) -> None:
        self.max_path = -999999999
        self.rotten_tomotoes = list()

    def is_in_matrix(self, point, width, height):
        if point[0] < 0 or point[1] < 0 or point[0] > height or point[1] > width:
            return False
        else:
            return True

    def get_neighbours(self, point):
        if point == (-1, -1):
            return self.rotten_tomotoes

        neigh = [(point[0], point[1]+1), (point[0], point[1]-1), (point[0]+1, point[1]), (point[0]-1, point[1])]
        # print(f'{point} | {neigh}')
        return neigh


    def bfs(self, root, visit_matrix, adj_mat, height, width):
        if visit_matrix[root[0]][root[1]] == 1 or adj_mat[root[0]][root[1]] in [1, 0]:
            if root == (-1, -1):
                pass
            else:
                return
        q = queue.Queue()
        q.put((root, -1))
        if root == (-1, -1):
            pass
        else:
            visit_matrix[root[0]][root[1]] = 1

        while not q.empty():
            node = q.get()
            nbrs = self.get_neighbours(node[0])
            print(f'point: {node} | {nbrs}')
            for n in nbrs:
                # print(n)
                if self.is_in_matrix(n, width, height) and visit_matrix[n[0]][n[1]]==0 and adj_mat[n[0]][n[1]]:
                    x = (n, node[1]+1)
                    q.put(x)
                    visit_matrix[n[0]][n[1]] = 1
                    # adj_mat[n[0]][n[1]] = 2
                    self.max_path = max(self.max_path, x[1])

    def solve(self, A):
        h = len(A)
        w = len(A[0])
        v_mat = [[0 for j in range(w)] for i in range(h)]
        for i in range(h):
            for j in range(w):
                if A[i][j] == 2:
                    self.rotten_tomotoes.append((i, j))

        # for i in range(h):
        #     for j in range(w):
        #         if A[i][j] == 2:
        self.bfs((-1, -1), v_mat, A, h-1, w-1)
        
        for i in range(h):
            for j in range(w):
                if A[i][j] == 1 and v_mat[i][j] != 1:
                    print('good tomatoe left!!!')
                    return -1
        
        ans = self.max_path
        print(f'ans is {ans}')
        self.__init__()
        return self.max_path


if __name__ == "__main__":
    a = [[0, 2, 2, 0, 2, 2, 2, 2, 2],
         [0, 0, 2, 1, 0, 0, 2, 1, 0],
         [2, 0, 2, 1, 0, 2, 0, 0, 2],
         [2, 0, 2, 2, 2, 1, 1, 0, 0],
         [2, 0, 0, 1, 1, 2, 0, 2, 0],
         [2, 1, 0, 2, 2, 0, 0, 0, 1],
         [2, 0, 1, 2, 0, 0, 2, 1, 1]]
    # a = [[2, 1, 1],
    #      [0, 0, 1],
    #      [2, 1, 1]]
    obj = Solution()
    obj.solve(a)
