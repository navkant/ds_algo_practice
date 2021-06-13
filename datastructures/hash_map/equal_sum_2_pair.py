class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        hash_map = dict()
        ret = []

        for i in range(len(A)):
            for j in range(i+1, len(A)):
                temp = A[i] + A[j]
                if temp in hash_map:
                    hash_map[temp] += [i, j]
                else:
                    hash_map[temp] = [i, j]
        print(hash_map)
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                temp = A[i] + A[j]
                if temp in hash_map:
                    templist = hash_map[temp]
                    if len(templist) >= 4:
                        ret += templist[0:2]
                        for k in range(2, len(templist), 2):
                            if templist[k] > ret[0] and templist[k] != ret[1] and templist[k+1] != ret[1]:
                                ret += templist[k:k+2]
                                return ret
                        if len(ret) < 4:
                            ret = []
        if len(ret) < 4:
            return []
        return ret


if __name__ == "__main__":
    # a = [3, 4, 7, 1, 2, 9, 8]
    a = [ 0, 0, 1, 0, 2, 1 ]
    print(a)
    print()
    obj = Solution()
    ret = obj.equal(a)
    print('ret is: ', ret)
