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
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        n = len(A)
        q = Queue()
        ans = [A[0]]

        for i in range(n):
            if i < B:
                if q.is_empty():
                    q.enqueue(i)
                else:
                    while not q.is_empty() and A[i] > A[q.last()]:
                        q.deque_last()
                    q.enqueue(i)

                    ans[0] = max(ans[0], A[q.last()])
            else:
                print(q.start, q.end)
                while not q.is_empty() and A[i] > A[q.last()]:
                    q.deque_last()

                while not q.is_empty() and q.front() + (B-1) < i:
                    q.dequeue()

                q.enqueue(i)
                ans.append(A[q.front()])

            print(f'i: {i} ', q.queue[q.start + 1:q.end + 1], ans)
        return ans


if __name__ == '__main__':
    a = [1,3,-1,-3,5,3,6,7]
    b = 3
    print(a)
    obj = Solution()
    ans = obj.slidingMaximum(a, b)
    print(f'ans is {ans}')