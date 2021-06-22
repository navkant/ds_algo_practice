class Solution:
    # @param A : list of list of chars
    def __init__(self) -> None:
        self.board = None
        self.width = None
        self.height = None
        self.visit_matrix = None
    
    def is_in_matrix(self, node):
        if node[0] < 0 or node[1] < 0 or node[0] >= self.height or node[1] >= self.width:
            return False
        else:
            return True

    def get_valid_nbors(self, node):
        neigh = [(node[0], node[1]+1), (node[0], node[1]-1), (node[0]+1, node[1]), (node[0]-1, node[1])]
        # print(f'{point} | {neigh}')
        valid_nbors = list()

        for n in neigh:
            if self.is_in_matrix(n) and self.visit_matrix[n[0]][n[1]] != 1 and self.board[n[0]][n[1]] == 'O':
                valid_nbors.append(n)
        return valid_nbors

    def dfs(self, node):
        self.visit_matrix[node[0]][node[1]] = 1
        self.board[node[0]][node[1]] = 'A'

        nbors = self.get_valid_nbors(node)
        for n in nbors:
            self.dfs(n)

    def on_boundary(self, node):
        if node[0] == 0 or node[1] == 0 or node[0] == self.height-1 or node[1] == self.width-1:
            return True
        else:
            return False

    def solve(self, A):
        self.board = A.copy()
        self.height = len(A)
        self.width = len(A[0])
        self.visit_matrix = [[0 for j in range(self.width)] for i in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                point = (i, j)
                if self.on_boundary(point) and self.board[point[0]][point[1]] == 'O':
                    self.dfs(point)
        
        for row in self.board:
            print(row)
        
        for i in range(self.height):
            for j in range(self.width):
                point = (i, j)
                if self.board[point[0]][point[1]] == 'O':
                    self.board[point[0]][point[1]] = 'X'
                if self.board[point[0]][point[1]] == 'A':
                    self.board[point[0]][point[1]] = 'O'

        print()
        for row in self.board:
            print(row)


if __name__ == "__main__":
    a = [['X', 'X', 'X', 'X' ],
         ['X', 'X', 'O', 'X' ],
         [ 'X', 'X', 'X', 'X' ],
         [ 'X', 'O', 'X', 'X' ]]
    obj = Solution()
    obj.solve(a)