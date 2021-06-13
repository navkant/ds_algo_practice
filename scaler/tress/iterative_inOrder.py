class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.stack = list()

    def iterative_inorder(self, root):
        node = root

        while node:
            self.stack.append(node)
            if node.left:
                node = node.left
            elif self.stack:
                # print(node.val, end=' ')
                while self.stack and self.stack[-1].right is None:
                    temp = self.stack.pop()
                    print(temp.val, end=' ')
                if self.stack:
                    temp = self.stack.pop()
                    node = temp.right
                    print(temp.val, end=' ')
                else:
                    break
            else:
                break

    def iterative_inorder_3(self, root):
        node = root

        while node or self.stack:
            if node:
                self.stack.append(node)
                node = node.left
            elif self.stack:
                temp = self.stack.pop()
                print(temp.val, end=' ')
                node = temp.right
            else:
                break

    def iterative_inorder_2(self, root):
        node = root

        while node or self.stack:
            if node:
                self.stack.append(node)
                node = node.left
            else:
                node = self.stack.pop()
                print(node.val, end=' ')
                node = node.right

    def solve(self, A):
        self.iterative_inorder(A)
        print()
        self.iterative_inorder_2(A)
        print()
        self.iterative_inorder_3(A)
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
