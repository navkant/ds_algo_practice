class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        timestamps = []

        for i in range(len(A)):
            timestamps.append((A[i], B[i]))

        timestamps = sorted(timestamps, key=lambda x: x[1])

        count = 1
        print(timestamps)
        job_done = timestamps[0]
        for i in range(1, len(timestamps)):
            if timestamps[i][0] >= job_done[1]:
                count += 1
                job_done = timestamps[i]

        return count


if __name__ == '__main__':
    a = [1, 5, 7, 1]
    b = [7, 8, 8, 8]
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')