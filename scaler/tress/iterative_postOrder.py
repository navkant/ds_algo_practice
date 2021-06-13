class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.stack = list()
        self.ans = []

    def iterative_postorder(self, root):
        node = root

        while node:
            l = [i.val for i in self.stack]
            print(f'stack: {l}')
            while node is not None:
                if node.right:
                    self.stack.append(node.right)
                self.stack.append(node)
                node = node.left

            while node is None and self.stack:
                l = [i.val for i in self.stack]
                print(f'    stack: {l}')
                top = self.stack.pop()
                if self.stack and top.right and top.right.val == self.stack[-1].val:
                    right = self.stack.pop()
                    self.stack.append(top)
                    node = right
                else:
                    # print(top.val, end=' ')
                    self.ans.append(top.val)
                    node = None

    def solve(self, A):
        self.iterative_postorder(A)
        return self.ans


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
    node10 = TreeNode(0)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node10

    node3.left = node5
    node3.right = node6

    node5.left = node7

    node6.left = node8
    node6.right = node9

    obj = Solution()
    ans = obj.solve(node1)
    print(f'ans is {ans}')
