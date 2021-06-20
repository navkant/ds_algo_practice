import queue


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer

    def dfs(self, root, visit_arr, ad_list):
        visit_arr[root] = 1
        for nbor in ad_list[root]:
            if visit_arr[nbor] == 0:
                self.dfs(nbor, visit_arr, ad_list)

    def solve(self, A, B):
        adj_list = {}
        visited = [0] * (A+1)
        for i in range(1, A+1):
            adj_list[i] = list()

        for edge in B:
            adj_list[edge[0]].append(edge[1])

        for k, v in adj_list.items():
            print(k, ':', v)

        self.dfs(1, visited, adj_list)
        print(visited)
        if visited[A]:
            return 1
        else:
            return 0


if __name__ == '__main__':
    a = 5
    b = [[1, 2],
         [4, 1],
         [2, 4],
         [3, 4],
         [5, 2],
         [1, 3]]
    obj = Solution()
    obj.solve(a, b)