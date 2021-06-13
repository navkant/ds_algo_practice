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
        x = self.queue[self.start]
        self.start += 1
        return x

    def deque_last(self):
        x = self.queue.pop()
        self.end -= 1
        return x

    def get_size(self):
        return self.end - self.start

    def front(self):
        return self.queue[self.start+1]

    def last(self):
        return self.queue[self.end]
