import sys


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        ans = sys.maxsize * -1
        summ = 0
        last_index = 0
        count = 0
        for i in range(len(A)):

            if A[i] > 0:
                summ += A[i]
                count += 1
            else:
                count = 0
                summ = 0

            if summ > ans:
                ans = summ
                last_index = i
                start_index = last_index - count + 1
            else:
                pass
        print(f'last_idx: {last_index}, start_idx: {start_index}, sum : {ans}')
        if ans != 0:
            return A[start_index:last_index+1]
        else:
            print('nvnf')
            final_count = sys.maxsize * -1
            count = 0
            for i in range(len(A)):
                if A[i] == 0:
                    count += 1
                else:
                    count = 0

                if count > final_count:
                    final_count = count
                    last_index = i

            start_index = last_index - final_count + 1
            print(f'last_idx: {last_index}, start_idx: {start_index}')
            return A[start_index:last_index+1]


if __name__ == '__main__':
    a = [ -846930886, -1714636915, 424238335, -1649760492 ]
    obj = Solution()
    ans = obj.maxset(a)
    print(f'ans is {ans}')