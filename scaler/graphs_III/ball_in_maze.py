# from heapq import heappop, heappush
import queue


class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def get_nbors(self, node, matrix,  visit_matrix):
        nbors = [([node[0], node[1]+1], 0), ([node[0]-1, node[1]], 1), ([node[0], node[1]-1], 2),([node[0]+1, node[1]], 3)]
        nbor_list = []
        for n, dir in nbors:
            print(n)
            if n[0] >= 0 and n[1] >= 0 and n[0] < len(matrix) and n[1] < len(matrix[0]):
                nbor_list.append((n, dir))
            else:
                pass
        return nbor_list
 
    def solve(self, A, B, C):
        h = len(A)
        w = len(A[0])

        visit_matrix = [[[0, 0, 0, 0] for j in range(w)] for i in range(h)]
        distance_matrix = [[float("inf") for j in range(w)] for i in range(h)]
        q = queue.Queue()

        for i in range(h):
            for j in range(w):
                if i == B[0] and j == B[1]:
                    q.put((0, -1, (i, j)))
                    distance_matrix[i][j] = 0
                else:
                    pass
        while not q.empty():
            distance, direction, node = q.get()
            if direction == -1:
                visit_matrix[node[0]][node[1]] = [1, 1, 1, 1]

            if direction == 0 and ((node[0] == 0 or node[0] == h-1 or node[1] == 0 or node[1] == w-1) or A[node[0]][node[1]+1] == 1):
                distance_matrix[node[0]][node[1]] = min(distance, distance_matrix[node[0]][node[1]])

            if direction == 1 and ((node[0] == 0 or node[0] == h-1 or node[1] == 0 or node[1] == w-1) or A[node[0]-1][node[1]] == 1):
                distance_matrix[node[0]][node[1]] = min(distance, distance_matrix[node[0]][node[1]])

            if direction == 2 and ((node[0] == 0 or node[0] == h-1 or node[1] == 0 or node[1] == w-1) or A[node[0]][node[1]-1] == 1):
                distance_matrix[node[0]][node[1]] = min(distance, distance_matrix[node[0]][node[1]])

            if direction == 3 and ((node[0] == 0 or node[0] == h-1 or node[1] == 0 or node[1] == w-1) or A[node[0]+1][node[1]] == 1):
                distance_matrix[node[0]][node[1]] = min(distance, distance_matrix[node[0]][node[1]])

            nbors = self.get_nbors(node, A, visit_matrix)
            visit_matrix[node[0]][node[1]][direction] = 1

            print(f"{node} | {nbors}")
            for n, dir in nbors:
                if sum(visit_matrix[n[0]][n[1]]) == 4 or A[n[0]][n[1]] == 1:
                    continue
                nbor_distance = distance + 1
                distance_matrix[n[0]][n[1]] = nbor_distance
                q.put((nbor_distance, dir, n))
                # heappush(hp, (nbor_distance, (n[0], n[1])))
        
        print(distance_matrix[C[0]][C[1]])
        if distance_matrix[C[0]][C[1]] == float('inf'):
            return -1
        else:
            return distance_matrix[C[0]][C[1]] 

        
if __name__ == "__main__":
    A = [[1, 1, 0, 1],
         [0, 0, 0, 1],
         [1, 0, 0, 1],
         [0, 0, 1, 0]]
    B = [1, 1]
    C = [3, 1]
    obj = Solution()
    obj.solve(A, B, C)
