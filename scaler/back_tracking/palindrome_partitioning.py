class Solution:
    # @param A : string
    # @return a list of list of strings
    def is_palindrome(self, string):
        i = 0
        n = len(string) - 1

        while True:
            if i == n:
                break
            if i + 1 == n:
                if string[i] == string[n]:
                    return True
                else:
                    return False

            if string[i] == string[n]:
                pass
            else:
                return False
            i += 1
            n -= 1
        return True

    def palindrome_partition_recurse(self, index, string, result, subset):
        if index > len(string):
            # print(subset)
            result.append([x for x in subset])
            return

        if self.is_palindrome(string[:index]):
            subset.append(string[:index])
            # print(subset)
            self.palindrome_partition_recurse(1, string[index:], result, subset)
            subset.pop()

        self.palindrome_partition_recurse(index+1, string, result, subset)

    def partition(self, A):
        ans = []
        self.palindrome_partition_recurse(1, A, ans, [])
        print(f'ans is {ans}')


if __name__ == '__main__':
    s = 'abbab'
    obj = Solution()
    obj.partition(s)
