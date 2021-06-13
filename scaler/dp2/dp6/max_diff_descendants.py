class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return an integer

    def __init__(self):
        self.maximun = -9999999999

    def get_children_array(self, value_array, edges_array):
        n = len(value_array)
        for i in range(len(edges_array)):
            edges_array[i][0] -= 1
            edges_array[i][1] -= 1
        
        children_map = dict()

        for i in range(n):
            children_map[i] = list()

        for edge in edges_array:
            children_map[edge[0]].append(edge[1])

        for k, v in children_map.items():
            print(k, v)
        
        return children_map
    
    def get_max_diff(self, root, value_array, children_map):

        minn = value_array[root]
        maxx = value_array[root]
        for child in children_map[root]:
            root_minn, root_maxx = self.get_max_diff(child, value_array, children_map)
            minn = min(minn, root_minn)
            maxx = max(maxx, root_maxx)
        
        self.maximun = max(max(abs(value_array[root] - minn), abs(value_array[root] - maxx)), self.maximun)
        return min(minn, value_array[root]), max(value_array[root], maxx)

    def solve(self, A, B):
        c_array = self.get_children_array(A, B)
        self.get_max_diff(1, A, c_array)
        print(f'ans is {self.maximun}')


if __name__ == '__main__':
    A = [-59, -33, 34, 0, 69, 24, -22, 58, 62, -36, 5, 45, -19]
    B = [[10, 6],
         [3, 2],
         [12, 7],
         [9, 5],
         [2, 1],
         [8, 3],
         [7, 1],
         [4, 2],
         [6, 3],
         [11, 4],
         [5, 3],
         [13, 11]]
    obj = Solution()
    obj.solve(A, B)