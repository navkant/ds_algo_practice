import sys


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        hash_map = {}
        summ = 0
        start_index = 0
        for i in range(len(A)):
            if A[i] < 0 or i == len(A)-1:
                if A[i] < 0 and i != len(A)-1:
                    if summ not in hash_map:
                        hash_map[summ] = (start_index, i-1)
                        start_index = i + 1
                        summ = 0
                        continue
                    else:
                        len_prev_sub_array = hash_map[summ][1] - hash_map[summ][0] + 1
                        print(f'prev: {len_prev_sub_array}')
                        len_curr_sub_array = i - start_index
                        print(f'curr: {len_curr_sub_array}')
                        if len_curr_sub_array > len_prev_sub_array:
                            hash_map[summ] = (start_index, i-1)
                        else:
                            pass
                        start_index = i + 1
                        summ = 0
                        continue
                elif A[i] >= 0 and i == len(A)-1:
                    summ += A[i]
                    if summ not in hash_map:
                        hash_map[summ] = (start_index, i)
                        start_index = i + 1
                        summ = 0
                        continue
                    else:
                        len_prev_sub_array = hash_map[summ][1] - hash_map[summ][0] + 1
                        print(f'prev: {len_prev_sub_array}')
                        len_curr_sub_array = i - start_index
                        print(f'curr: {len_curr_sub_array}')
                        if len_curr_sub_array > len_prev_sub_array:
                            hash_map[summ] = (start_index, i)
                        else:
                            pass
                else:
                    hash_map[summ] = (start_index, i-1)

            else:
                summ += A[i]
        print(hash_map)

        maxx = sys.maxsize * -1
        for k in hash_map.keys():
            maxx = max(maxx, k)

        return A[hash_map[maxx][0]:hash_map[maxx][1]+1]


if __name__ == '__main__':
    a = [ 0, 0, -1, 0 ]
    print(a)
    obj = Solution()
    ans = obj.maxset(a)
    print('ans is: ', ans)

