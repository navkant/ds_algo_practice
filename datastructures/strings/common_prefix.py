class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        first = A[0]
        common_substring = ''
        for i in range(1, len(A)):
            substring = ''
            for j in range(min(len(first), len(A[i]))):
                if A[i][j] == first[j]:
                    substring += A[i][j]
                else:
                    break
            if common_substring and (len(substring) < len(common_substring)):
                common_substring = substring
            elif not common_substring and substring:
                common_substring = substring
            else:
                pass
        return common_substring


if __name__ == "__main__":
    a = ["abcdefgh", "aefghijk", "abcefgh"]
    print(a)
    obj = Solution()
    ans = obj.longestCommonPrefix(a)
    print('ans is: ', ans)
