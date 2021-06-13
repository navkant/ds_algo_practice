class Solution:
    # @param A : list of integers
    # @return a list of list of integers

    # def subsetDupRec(self, array, start, output, ans):
    #     if output not in ans:
    #         ans.append(output)
    #     if start == len(array):
    #         return
    #
    #     output2 = output.copy()
    #     # output2.insert(0, array[start])
    #     output2.append(array[start])
    #     self.subsetDupRec(array, start + 1, output2, ans)
    #     self.subsetDupRec(array, start+1, output, ans)
    #     return ans
    #
    # def subsetsWithDup(self, A):
    #     if len(A) == 0:
    #         return [[]]
    #     A.sort()
    #     ans = self.subsetDupRec(A, 0, [], [])
    #     return ans

    def subsets(self, s):
        s.sort()
        r = [[]]
        for e in s:
            print(r)
            r += [x+[e] for x in r]
        return sorted(r)


if __name__ == '__main__':
    a = [1, 2, 3]
    print(a)
    obj = Solution()
    ans = obj.subsets(a)
    print('ans is: ', ans)


def compact_spaces(self, string):
    output_string = ""
    for char in string:
        if char != " " or ( output_string and output_string[-1] != " "):
            output_string += char
    return output_string


#     class Solution:
#         # @param A : list of integers
#         # @param B : integer
#         # @param C : integer
#         # @return an integer
#         def solve(self, A, B, C):
#             count = 0
#             n = len(A)
#             for i in range(n):
#                 sum = 0
#                 for j in range(i, n):
#                     sum += A[j]
#
#                     if B <= sum <= C:
#                         count += 1
#                     else:
#                         pass
#             return count
#
#
#     [0, 0, 0, 0]
#
#     #  A = [1, 2, 3]
#     #  B = 4
#     #  C = 6
#
#     # Sol-1 Iterative
#     # Time : O(n^2)
#     # Space : O(1)
#
#     1
#     2
#     3
#     4
#     0
#     1
#     2
#     3
#     [1, 2][3, 4]
#
#     {[bucket_num * sqrt(n) + 1], [bucket_num + sqrt(n)]}
#
#     [1][2
#     2]
#     1
#     2
#
# n
# each
# bucket = sqrt(n) * sqrt(n)
#
# [sqrt(n) sqrt(n) sqrt(n) sqrt(n)]
# [[---][---][---]]
#
# # pref_sum = [1, 3, 6]
