class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.stack = list()

    def iterative_preorder(self, root):
        node = root

        while node:
            # if not node.left and node.right and not self.stack:
            #     break
            print(node.val, end=' ')
            self.stack.append(node)
            if node.left:
                node = node.left
            elif self.stack:
                while self.stack and self.stack[-1].right is None:
                    temp = self.stack.pop()
                if self.stack:
                    temp = self.stack.pop()
                    node = temp.right
                else:
                    break
            else:
                break

    def pre_order(self, root):
        node = root
        self.stack.append(root)

        while self.stack:
            node = self.stack.pop()
            print(node.val, end=' ')
            if node.right is not None:
                self.stack.append(node.right)
            if node.left is not None:
                self.stack.append(node.left)

    def solve(self, A):
        self.iterative_preorder(A)
        return 0


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
    ans = obj.solve(node1)
