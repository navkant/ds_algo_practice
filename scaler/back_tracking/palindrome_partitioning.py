class Solution:
    # @param A : string
    # @return a list of list of strings
    def is_palindrome(self, string1):
        if len(string1) == 1:
            return True
        if len(string1) == 0:
            return False

        i = 0
        n = len(string1) - 1

        while True:
            if i == n:
                break
            if i + 1 == n:
                if string1[i] == string1[n]:
                    return True
                else:
                    return False

            if string1[i] == string1[n]:
                pass
            else:
                return False
            i += 1
            n -= 1
        return True

    def palindrome_partition_recurse(self, i, string, result, subset):
        # print(f'i: {i}')
        if i == len(string):
            # print(subset)
            result.append([x for x in subset])
            return

        for j in range(i, len(string)):
            # print(f'string: {string[i:j+1]}')
            if self.is_palindrome(string[i:j+1]):
                # print(f'string {string[i:j]} is palindrome')
                subset.append(string[i:j+1])
                self.palindrome_partition_recurse(j+1, string, result, subset)
                subset.pop()

    def partition(self, A):
        ans = []
        self.palindrome_partition_recurse(0, A, ans, [])
        for row in ans:
            print(row)


if __name__ == '__main__':
    s = 'abbab'
    obj = Solution()
    obj.partition(s)
