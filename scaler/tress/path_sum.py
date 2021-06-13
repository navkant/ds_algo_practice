
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def __init__(self):
        self.ans = 0

    def check_sum(self, root, summ):
        if root.left is None and root.right is None:
            if summ - root.val == 0:
                self.ans = 1
            else:
                pass
            return

        if root.left is not None:
            self.check_sum(root.left, summ - root.val)
        else:
            pass

        if root.right is not None:
            self.check_sum(root.right, summ - root.val)

    def hasPathSum(self, A, B):
        self.check_sum(A, B)
        return self.ans


if __name__ == '__main__':
    obj = Solution()
    root = TreeNode(1000)
    left_node = TreeNode(200)
    root.left = left_node

    ans = obj.hasPathSum(root, 1000)
    print(f'ans is {ans}')
