from Queue import Queue

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        queue = Queue()
        ans = [0]

        for i in range(n):
            if i < B:
                if A[i] < 0:
                    queue.enqueue(i)
                else:
                    pass

                if not queue.is_empty():
                    ans[0] = A[queue.front()]
                else:
                    pass
            else:
                if A[i] < 0:
                    queue.enqueue(i)

                while not queue.is_empty() and queue.front() + (B-1) < i:
                    queue.dequeue()

                if queue.is_empty():
                    ans.append(0)
                else:
                    ans.append(A[queue.front()])

            print(f'i: {i} ', queue.queue[queue.start + 1:queue.end + 1], ans)
        return ans


if __name__ == '__main__':
    a = [-1, 2, 3, -4, 5]
    b = 2
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
