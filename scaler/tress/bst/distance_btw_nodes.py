# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def __init__(self):
        self.stack = list()
        self.lca_array = list()

    def get_lca(self, root, key):
        if root is None:
            return
        self.stack.append(root.val)

        if root.val == key:
            self.lca_array = self.stack.copy()
            return

        self.get_lca(root.left, key)
        self.get_lca(root.right, key)
        self.stack.pop()

    def get_distance(self, node, key):

        distance = 0
        while node.val != key:
            if key < node.val:
                node = node.left
            else:
                node = node.right
            distance += 1
        return distance

    def solve(self, A, B, C):
        self.get_lca(A, B)
        lca1 = self.lca_array

        self.lca_array = list()
        self.get_lca(A, C)
        lca2 = self.lca_array

        for i in range(len(lca1)):
            if lca1[i] != lca2[i]:
                break

        lca_element = lca1[i - 1]

        d1 = self.get_distance(A, B)
        d2 = self.get_distance(A, C)
        d3 = self.get_distance(A, lca_element)

        return d1 + d2 - (2 * d3)


if __name__ == '__main__':
    pass