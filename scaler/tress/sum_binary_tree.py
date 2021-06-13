# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def check_sum_binary_tree(self, root):
        if root.left is None and root.right is None:
            return 1, root.val

        if root.left is not None:
            left_subtree = self.check_sum_binary_tree(root.left)
        else:
            left_subtree = ()

        if root.right is not None:
            right_subtree = self.check_sum_binary_tree(root.right)
        else:
            right_subtree = ()

        if left_subtree and right_subtree:
            summ = left_subtree[1] + right_subtree[1]
            if summ == root.val:
                return 1, summ + root.val
            else:
                return 0, summ + root.val

        if left_subtree:
            if left_subtree[1] == root.val:
                return 1, left_subtree[1] + root.val
            else:
                return 0, left_subtree[1] + root.val

        if right_subtree:
            if right_subtree[1] == root.val:
                return 1, right_subtree[1] + root.val
            else:
                return 0, right_subtree[1] + root.val

    def solve(self, A):
        return self.check_sum_binary_tree(A)[0]
