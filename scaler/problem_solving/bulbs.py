class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        hash_map = {'on': 0, 'off': 0}

        for i in A:
            if i == 0:
                hash_map['off'] += 1
            else:
                hash_map['on'] += 1

        i = 0
        count = 0
        toggle_count = 0
        while True:
            if i == len(A) or hash_map['off'] == 0:
                break
            if A[i] == 0 and i == 0:
                count += 1
                toggle_count += 1
                temp = hash_map['on']
                hash_map['on'] = hash_map['off']
                hash_map['off'] = temp
            elif A[i] == 0 and toggle_count % 2 == 0:
                count += 1
                toggle_count += 1
                temp = hash_map['on']
                hash_map['on'] = hash_map['off']
                hash_map['off'] = temp - 1
            elif A[i] == 1 and toggle_count % 2 != 0:
                count += 1
                toggle_count += 1
                temp = hash_map['on']
                hash_map['on'] = hash_map['off']
                hash_map['off'] = temp - 1
            i += 1
        print(hash_map)
        return count


if __name__ == '__main__':
    a = [0, 1, 0, 1]
    obj = Solution()
    ans = obj.bulbs(a)
    print(f'ans is: {ans}')
    a = [1, 0, 0, 0, 1]
    s = [1, 1, 1, 1, 2]
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]