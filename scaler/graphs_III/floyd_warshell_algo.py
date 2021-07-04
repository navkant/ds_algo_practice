class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        h = len(A)
        w = len(A[0])
        total_nodes = len(A)
        dist_matrix = [[float('inf') for j in range(w)] for i in range(h)]

        for int_node in range(total_nodes):
            for start in range(total_nodes):
                for end in range(total_nodes):
                    dist_matrix[start][end] = min(A[start][end], A[start][int_node] + A[int_node][end])

        for int_node in range(total_nodes):
            for start in range(total_nodes):
                for end in range(total_nodes):
                    dist_matrix[start][end] = min(A[start][end], A[start][int_node] + A[int_node][end])
    
        for row in dist_matrix:
            print(row)


if __name__ == "__main__":
    A = [[0 , 50 , 39],
         [-1 , 0 , 1],
         [-1 , 10 , 0]]
    
    obj = Solution()
    obj.solve(A)
