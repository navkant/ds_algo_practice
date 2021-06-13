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
    # @param A : string
    # @return a strings
    def solve(self, A):
        q = Queue()
        n = len(A)
        ans = A[0]
        freq_map = dict()

        q.enqueue(A[0])
        freq_map[A[0]] = 1

        for i in range(1, n):
            print(i, q.queue[q.start+1: q.end+1], freq_map, ans)
            # if q.is_empty():
            #     q.enqueue(A[i])
            #     if A[i] not in freq_map:
            #         freq_map[A[i]] = 1
            #     else:
            #         freq_map[A[i]] += 1
            #     ans = ans + '#'
            # else:
            if not q.is_empty() and A[i] == q.front():
                q.dequeue()
            else:
                if A[i] not in freq_map:
                    freq_map[A[i]] = 1
                    q.enqueue(A[i])
                else:
                    freq_map[A[i]] += 1

            if q.is_empty():
                ans = ans + '#'
            else:
                # if i > 45:
                #     print(not q.is_empty(), freq_map[q.front()] > 1)
                #     print(not q.is_empty() and freq_map[q.front()] > 1)
                while not q.is_empty() and freq_map[q.front()] > 1:
                    # if i > 48:
                    #     import pdb; pdb.set_trace()
                    q.dequeue()
                ans = ans + q.front()

        return ans


if __name__ == '__main__':
    a = 'jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl'
    print(a)
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
    print('expe is jjjjjyyyyr')