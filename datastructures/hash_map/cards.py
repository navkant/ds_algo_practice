class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        hash_map = dict()
        for i in A:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        if len(list(hash_map.keys())) > 2:
            return "LOSE"
        else:
            for number in hash_map.keys():
                freq = hash_map[number]
                if freq == len(A) / 2:
                    return "WIN"
                else:
                    return "LOSE"


if __name__ == "__main__":
    a = [ 1, 1, 2, 2, 2 ]
    obj = Solution()
    ans = obj.solve(a)
    print(ans)