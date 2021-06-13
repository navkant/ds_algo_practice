# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
sys.setrecursionlimit(10**5)

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree

    def concatenate(self, leftList, rightList):
        if leftList is None:
            return rightList
        if rightList is None:
            return leftList

        left_last = leftList.left
        right_last = rightList.left
        if left_last is not None:
            left_last.right = rightList
        rightList.left = left_last
        leftList.left = right_last
        if right_last is not None:
            right_last.right = leftList

        return leftList

    def flatten_tree(self, root):
        if root is None:
            return None

        left = self.flatten_tree(root.left)
        right = self.flatten_tree(root.right)
        root.left = root
        root.right = root

        return self.concatenate(self.concatenate(left, root), right)

    def solve(self, A):
        return self.flatten_tree(A)


if __name__ == '__main__':
    pass