class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.is_possible = False

    def get_adj_list(self, arr):
        adj_list = {}
        n = len(arr)
        for i in range(1, n+1):
            adj_list[i] = list()

        for i in range(1, n):
            adj_list[arr[i]].append(i+1)
        
        for k, v in adj_list.items():
            print(k, v)
        print()
        return adj_list
    
    def dfs(self, node, adj_arr, visit_array, destination):
        visit_array[node] = True
        print(f'{node}: {destination}')
        if node == destination:
            self.is_possible = True

        neighbours = adj_arr[node]
        print(f'{node} | {neighbours}')
        for n in neighbours:
            if not visit_array[n]:
                self.dfs(n, adj_arr, visit_array, destination)
            else:
                pass

    def solve(self, A, B, C):
        ad_list = self.get_adj_list(A)
        v_array = [False for i in range(len(A)+1)]
        self.dfs(C, ad_list, v_array, B)
        print(f'ans is {self.is_possible}')



if __name__ == "__main__":
    A = [1, 1, 1, 3, 3, 4, 6, 5, 3, 3]
    # A = [1, 1, 2]
    B = 10
    C = 3
    obj = Solution()
    obj.solve(A, B, C)
