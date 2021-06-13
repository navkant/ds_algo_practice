class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
        self.summ = 0

    def add_common_nodes(self, root1, root2):

        while True:
            if root1:
                self.stack1.append(root1)
                root1 = root1.left
            elif root2:
                self.stack2.append(root2)
                root2 = root2.left
            elif self.stack1 and self.stack2:
                node1 = self.stack1[-1]
                node2 = self.stack2[-1]

                if node1.val == node2.val:
                    self.stack1.pop()
                    self.stack2.pop()
                    self.summ += node2.val
                    self.summ %= 1000000007
                elif node1.val > node2.val:
                    temp = self.stack2.pop()
                    root2 = temp.right
                    root1 = None
                else:
                    temp = self.stack1.pop()
                    root1 = temp.right
                    root2 = None
            else:
                break

            print(f'Tree 1: {self.stack1}')

    def solve(self, A, B):
        pass
