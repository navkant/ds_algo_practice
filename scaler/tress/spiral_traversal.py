from collections import deque


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


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
    def __init__(self):
        pass

    def zigzagLevelOrder(self, A):
        q = Queue()

        q.enqueue(A)
        direction = 0  # left to right

        ans = []

        while not q.is_empty():
            level_size = q.get_size()
            
            values = []
            for i in range(level_size):
                front = q.dequeue()
                values.append(front.val)
                if front.left:
                    q.enqueue(front.left)
                if front.right:
                    q.enqueue(front.right)

            direction = not direction

            row = []
            if direction == 1:
                for i in range(len(values)):
                    row.append(values[i])
            else:
                for i in range(len(values)-1, -1, -1):
                    row.append(values[i])
            ans.append(row)

        return ans
