class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        queue = ['1', '2']

        for i in range(A):
            queue.append(queue[i] + '1')
            queue.append(queue[i] + '2')

        return queue[A-1] + queue[A-1][::-1]


if __name__ == '__main__':
    a = 5
    obj = Solution()
    ans = obj.solve(a)
    print(f'ans is {ans}')
