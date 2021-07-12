class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of list of integers
    # @param D : integer
    # @return an integer

    def find_set(self, node):
        if self.parent_array[node] == node:
            return node
        p = self.find_set(self.parent_array[node])
        self.parent_array[node] = p
        return p

    def make_union(self, node1, node2):
        s1 = self.find_set(node1)
        s2 = self.find_set(node2)

        if s1 == s2:
            return False
        else:
            if self.height_array[s1] < self.height_array[s2]:
                s1, s2 = s2, s1
            self.parent_array[s2] = s1
            self.strength_array[s1] += self.B_array[s2]
            if self.height_array[s1] == self.height_array[s2]:
                self.height_array[s1] += 1

    def solve(self, A, B, C, D):
        B.insert(0, 0)
        self.B_array = B
        self.strength_array = B
        self.parent_array = [i for i in range(A+1)]
        self.height_array = [0 for i in range(A+1)]

        for i in C:
            self.make_union(i[0], i[1])

        count = 0

        for strnth in self.strength_array:
            if strnth >= D:
                count += 1
        print(count)


if __name__ == '__main__':
    A = 7
    B = [1, 6, 7, 2, 9, 4, 5]
    C = [[1, 2],
         [2, 3],
         [5, 6],
         [5, 7]]
    D = 12
    obj = Solution()
    obj.solve(A, B, C, D)
