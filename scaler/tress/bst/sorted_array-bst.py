# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree

    def create_bbst(self, root, data):
        if root.val > data:
            if not root.left:
                newNode = TreeNode(data)
                root.left = newNode
                return
            self.create_bbst(root.left, data)

        elif root.val < data:
            if not root.right:
                newNode = TreeNode(data)
                root.right = newNode
                return
            self.create_bbst(root.right, data)

    def sortedArrayToBST(self, A):
        n = len(A)
        mid = n // 2

        rootNode = TreeNode(A[mid])

        for i in range(mid):
            self.create_bbst(rootNode, A[i])

        for i in range(mid + 1, n):
            self.create_bbst(rootNode, A[i])

        return rootNode

    def pre_order(self, root):
        if root is None:
            return

        self.pre_order(root.left)
        print(root.val, end=' ')
        self.pre_order(root.right)


if __name__ == '__main__':
    a = [0,1,2,3,4,5]

    obj = Solution()
    root = obj.sortedArrayToBST(a)
    obj.pre_order(root)
