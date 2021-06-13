# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.ans = 0
        self.total_sum = 0

    def tree_sum(self, root):
        if root is None:
            return 0

        value = root.val
        left_sum = self.tree_sum(root.left)
        right_sum = self.tree_sum(root.right)
        return value + left_sum + right_sum

    def equal_tree(self, root):
        if root is None:
            return 0

        value = root.val

        left_s = self.equal_tree(root.left)
        right_s = self.equal_tree(root.right)

        subtree_sum = value + left_s + right_s

        if subtree_sum == self.total_sum // 2:
            self.ans = 1
        else:
            pass
        return subtree_sum

    def solve(self, A):
        summ = self.tree_sum(A)
        self.total_sum = summ
        self.equal_tree(A)
        return self.ans


if __name__ == '__main__':
    node1 = TreeNode(10)
    node2 = TreeNode(20)
    node3 = TreeNode(5)
    node4 = TreeNode(6)
    node5 = TreeNode(1)
    node6 = TreeNode(27)
    node7 = TreeNode(3)
    # node8 = TreeNode(8)
    # node9 = TreeNode(9)

    node1.left = node2
    node1.right = node3

    node3.left = node4
    node3.right = node5

    node4.left = node6
    node4.right = node7

    obj = Solution()
    ans = obj.solve(node1)
    print(f'ans is {ans}')
