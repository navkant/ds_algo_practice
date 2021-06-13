class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer

    def find_ans(self, root, val_arr, c_map, g_map, dp):
        c1 = 0

        if dp[root] != -1:
            return dp[root]
        
        for child in c_map[root]:
            c1 += self.find_ans(child, val_arr, c_map, g_map, dp)
        
        c2 = val_arr[root]
        for ggc in g_map[root]:
            c2 += self.find_ans(ggc, val_arr, c_map, g_map, dp)
        
        print()
        print(f'root: {root}: c1: {c1} c2: {c2}')

        ans = max(c1, c2)
        dp[root] = ans
        return ans


    def find_valueable_node(self, tree, value_array):
        children_map = {}
        ggc_map = {}
        n = len(tree)

        for i in range(n):
            children_map[i] = list()
            ggc_map[i] = list()

        for i in range(1, n):
            children_map[tree[i]].append(i)
            if tree[i] != -1 and tree[tree[i]] != -1 and tree[tree[tree[i]]] != -1:
               ggc_map[tree[tree[tree[i]]]].append(i)
            else:
                pass
 
        dp_arr = [-1] * n
        
        return self.find_ans(0, value_array, children_map, ggc_map, dp_arr)

            
    def solve(self, A, B):
        n = len(A)
        for i in range(n):
            A[i] -= 1
        print(A)
        ans = self.find_valueable_node(A, B)
        print(f'recursive ans is {ans}')


if __name__ == '__main__':
    a = [0, 1, 1, 1, 3, 3, 6, 6]
    b = [1, 2, 3, 4, 5, 100, 7, 8]
    obj = Solution()
    obj.solve(a, b)
