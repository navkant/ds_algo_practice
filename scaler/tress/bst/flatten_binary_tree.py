# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree

    def flatten_tree(self, root):
        if root is None:
            return

        self.flatten_tree(root.left)
        self.flatten_tree(root.right)
        temp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = temp


    def flatten(self, A):
        self.flatten_tree(A)
        return A
