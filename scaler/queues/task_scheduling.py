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


class Solution:
    # @param A : list of integers TASKS
    # @param B : list of integers ORDER
    # @return an integer
    def solve(self, A, B):
        order_q = Queue()
        for i in B:
            order_q.enqueue(i)

        task_q = Queue()
        for j in A:
            task_q.enqueue(j)

        cycles = 0
        while not task_q.is_empty():
            curr_task = task_q.front()

            if curr_task == order_q.front():
                task_q.dequeue()
                order_q.dequeue()
            else:
                task_q.dequeue()
                task_q.enqueue(curr_task)

            cycles += 1
        return cycles


if __name__ == '__main__':
    a = [2, 3, 1, 5, 4]
    b = [1, 3, 5, 4, 2]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
