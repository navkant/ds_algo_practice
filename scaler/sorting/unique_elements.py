class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hash_map = dict()
        
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        elements = []
        for k in hash_map.keys():
            if hash_map[k] == 1:
                continue
            else:
                elements.extend([k] * hash_map[k])
        print(elements)
        step = 0
        for rep_ele in elements:
            step += 1
            new_no = rep_ele + 1
            while new_no in hash_map:
                new_no += 1
                step += 1
            hash_map[new_no] = 1

        return step

    def optimized_approach(self, A):
        n = len(A)
        A.sort()
        i=0
        j=0
        steps = 0

        while j < n:
            if i >= A[j]:
                steps += i - A[j]
                i += 1
                j += 1
            else:
                i = A[j] + 1
                j += 1

        return steps


if __name__ == '__main__':
    a = [0]
    obj = Solution()
    ans = obj.optimized_approach(a)
    print(f'ans is {ans}')