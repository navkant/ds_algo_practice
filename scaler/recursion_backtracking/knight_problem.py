class Solution:
    def __init__(self, N):
        self.A = [[-1 for i in range(N)] for j in range(N)]
        self.X = N
        self.Y = N

    def is_valid_cell(self, x, y):
        if 0 <= x < self.X and 0 <= y < self.Y:
            return True
        else:
            return False

    def get_possible_moves(self, x, y):
        moves_list = list()
        moves_list.append((x-2, y+1))      # up right
        moves_list.append((x-2, y-1))      # up left
        moves_list.append((x-1, y-2))      # left up
        moves_list.append((x+1, y-2))      # left down
        moves_list.append((x+2, y-1))      # down left
        moves_list.append((x+2, y+1))      # down right
        moves_list.append((x+1, y+2))      # right down
        moves_list.append((x-1, y+2))      # right up

        possible_moves_list = list()
        for cell in moves_list:
            if self.is_valid_cell(cell[0], cell[1]):
                possible_moves_list.append(cell)

        return possible_moves_list

    def recurse_back_track(self, x, y, count):
        if self.A[x][y] == -1:
            self.A[x][y] = count + 1
            if self.A[x][y] == (self.X ** 2) - 1:
                return True
            else:
                possible_moves = self.get_possible_moves(x, y)
                for pos in possible_moves:
                    result = self.recurse_back_track(pos[0], pos[1], self.A[x][y])
                    if result:
                        return result
                    else:
                        pass
                self.A[x][y] = -1
            return False
        else:
            return False

    def solve(self):
        R = self.recurse_back_track(0, 0, -1)
        return R


if __name__ == '__main__':
    a = 8
    obj = Solution(a)
    ans = obj.solve()
    print(f'ans is: {ans}')

    for i in obj.A:
        print(i)
