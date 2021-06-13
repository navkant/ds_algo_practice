# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None


class Queue:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)
        self.end += 1

    def is_empty(self):
        if self.start == self.end:
            return True
        return False

    def dequeue(self):
        self.start += 1
        x = self.queue[self.start]
        return x

    def get_size(self):
        return self.end - self.start


class Solution:
    # @param A : root node of tree
    # @return a list of list of integers

    def levelOrder(self, A):
        if A is None:
            return []

        q = Queue()
        q.enqueue(A)
        ans = []
        ans.append([A])

        while not q.is_empty():
            level_array = []
            level_size = q.get_size()
            for i in range(level_size):
                x = q.dequeue()
                level_array.append(x.val)
                if x.left:
                    q.enqueue(x.left)
                if x.right:
                    q.enqueue(x.right)
            ans.append(level_array)

        return ans







