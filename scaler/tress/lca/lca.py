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
        self.lca_array = None

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

    def lca(self, A):
        self.get_lca(A, 7)
        return self.lca_array


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node1.left = node2
    node1.right = node3

    node2.left = node4

    node3.left = node5
    node3.right = node6

    node5.left = node7

    node6.left = node8
    node6.right = node9

    obj = Solution()
    ans = obj.lca(node1)
    print(f'ans is {ans}')
