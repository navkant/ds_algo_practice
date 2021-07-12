class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    def __init__(self):
        pass

    def rec_permute(self, array, result, subarray):
        if len(array) == 0:
            if subarray not in result:
                result.append(subarray)
            else:
                pass
            return

        for i in range(len(array)):
            first_element = array[i]
            b = []
            for j in range(i):
                b.append(array[j])
            for j in range(i+1, len(array)):
                b.append(array[j])
            self.rec_permute(b, result, subarray + [first_element])

    def generatePerms(self, arr, currentPerm, allPerms, usedInds):
        if len(currentPerm) == len(arr):
            # allPerms.append(currentPerm)
            allPerms.append([num for num in currentPerm])

        usedVals = set()
        for i in range(len(arr)):
            if i not in usedInds and not arr[i] in usedVals:  # second check to avoid duplicates
                usedVals.add(arr[i])
                usedInds.add(i)
                currentPerm.append(arr[i])
                self.generatePerms(arr, currentPerm, allPerms, usedInds)
                usedInds.remove(i)
                currentPerm.pop()

    def permute(self, A):
        all_perm = []
        self.generatePerms(A, [], all_perm, set())
        print(all_perm)


if __name__ == '__main__':
    a = [1, 1, 2]
    obj = Solution()
    ans = obj.permute(a)
    print(f'ans is {ans}')
