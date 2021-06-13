class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def generate_hash_map(self, string):
        hash_map = dict()
        for i in string:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        return hash_map

    def solve(self, A, B):
        m = len(A)
        n = len(B)
        a_map = self.generate_hash_map(A)
        window_map = dict()
        i = 0
        count = 0

        while True:
            if i >= n:
                break

            if i < m:
                if B[i] not in window_map:
                    window_map[B[i]] = 1
                else:
                    window_map[B[i]] += 1
            else:

                window_map[B[i]] = window_map.get(B[i], 0) + 1
                start = i - len(A)
                if B[start] in window_map:
                    if window_map[B[start]] > 1:
                        window_map[B[start]] -= 1
                    else:
                        window_map.pop(B[start])

            if window_map == a_map:
                count += 1

            i += 1

        return count


if __name__ == '__main__':
    a = 'abc'
    b = 'abcbacabc'
    obj = Solution()
    ans = obj.solve(a, b)
    print(f'ans is {ans}')
