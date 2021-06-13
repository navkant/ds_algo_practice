# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

# class Solution:
#     # @param A : root node of tree
#     # @return an integer
#     def __init__(self):
#         self.ans = 0
#
#     def check(self, root):
#         if root.left is None and root.right is None:
#             return (1, root.val, root.val, True)
#
#         if root.left:
#             left_tree = self.check(root.left)
#         else:
#             left_tree = ()
#
#         if root.right:
#             right_tree = self.check(root.right)
#         else:
#             right_tree = ()
#
#         if left_tree and right_tree:
#             size = left_tree[0] + right_tree[0] + 1
#             if left_tree[3] and right_tree[3]:
#                 if left_tree[2] < root.val < right_tree[1]:
#                     return (size, left_tree[1], right_tree[2], True)
#                 else:
#                     return (size, left_tree[1], right_tree[2], False)
#             else:
#                 return (size, left_tree[1], right_tree[2], False)
#
#         elif left_tree:
#             if left_tree[3]:
#                 if left_tree[2] < root.val:
#                     return (left_tree[0], left_tree[1], root.val, True)
#                 else:
#                     return (left_tree[0], left_tree[1], root.val, False)
#             else:
#                 return (left_tree[0], left_tree[1], root.val, False)
#
#         elif right_tree:
#             if right_tree[3]:
#                 if root.val < right_tree[1]:
#                     return (right_tree[0], root.val, right_tree[2], True)
#                 else:
#                     return (right_tree[0], root.val, right_tree[2], False)
#             else:
#                 return (right_tree[0], root.val, right_tree[2], False)
#
#     def solve(self, A):
#         return self.check(A)[0]


# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.ans = 0

    def check(self, root):
        if root is None:
            return 0, -999999999999, 999999999999, True

        if root.left is None and root.right is None:
            return (1, root.val, root.val, True)

        if root.left:
            left_tree = self.check(root.left)
        else:
            left_tree = ()

        if root.right:
            right_tree = self.check(root.right)
        else:
            right_tree = ()

        if left_tree and right_tree:
            left_size = left_tree[0]
            right_size = right_tree[0]
            if left_tree[3] and right_tree[3]:
                if left_tree[2] < root.val < right_tree[1]:
                    size = left_size + right_size + 1
                    return size, left_tree[1], right_tree[2], True
                else:
                    return max(left_size, right_size), min(left_tree[1], root.val), max(right_tree[2], root.val), False
            else:
                return max(left_size, right_size), min(left_tree[1], root.val), max(right_tree[2], root.val), False

        elif left_tree:
            if left_tree[3]:
                if left_tree[2] < root.val:
                    return left_tree[0]+1, left_tree[1], root.val, True
                else:
                    return left_tree[0], min(left_tree[1], root.val), max(root.val, left_tree[2]), False
            else:
                return left_tree[0], min(left_tree[1], root.val), max(root.val, left_tree[2]), False

        elif right_tree:
            if right_tree[3]:
                if root.val < right_tree[1]:
                    return right_tree[0]+1, root.val, right_tree[2], True
                else:
                    return right_tree[0], min(root.val, right_tree[1]), max(right_tree[2], root.val), False
            else:
                return right_tree[0], min(root.val, right_tree[1]), max(right_tree[2], root.val), False

    def solve(self, A):
        return self.check(A)[0]


