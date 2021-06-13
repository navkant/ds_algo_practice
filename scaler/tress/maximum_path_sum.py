# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def max_path_sum_rec(self, root):
        if root is None:
            return 0
        left = self.max_path_sum_rec(root.left)
        right = self.max_path_sum_rec(root.right)

        return max(0, left+root.val, right+root.val)

    def maxPathSum(self, A):
        return self.max_path_sum_rec(A)


if __name__ == '__main__':
    root = 0
    obj = Solution()
    ans = obj.maxPathSum(root)
    print(f'ans is {ans}')
