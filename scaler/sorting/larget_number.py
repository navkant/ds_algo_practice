from fractions import Fraction

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        a = sorted(A, key = lambda x: Fraction(x, 10**len(str(x))-1), reverse=True)
        print(a)
        i = 0
        while i < len(A)-1:
            if a[i] != 0:
                break
            i += 1

        ret = map(lambda x: str(x), a[i:])
        return ''.join(ret)


if __name__ == '__main__':
    a = [ 8, 89 ]
    obj = Solution()
    ans = obj.largestNumber(a)
    print(f'ans is {ans}')

#
# Given two binary strings A and B of size N.
#
# You can perform the following operations:
#
# Select any two characters in string A and swap the characters.
# Select any two characters in string B and swap the characters.
# Select a character in string A and select a character in string B. Swap the characters from both strings.
# Find and return the minimum number of operations required to make the strings equal. If not possible return -1.
#
#
#
# Problem Constraints
# 1 <= N <= 5 * 105
#
# A and B only consist of '0' and '1'.
#
#
#
# Input Format
# First argument is a string A of size N.
#
# Second argument is an string B of size N.
#
#
#
# Output Format
# Return an integer denoting the minimum number of operations required to make the strings equal if possible, else return -1.
#
#
#
# Example Input
# Input 1:
#
#  A = "1101"
#  B = "0100"
# Input 2:
#
#  A = "111"
#  B = "000"
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  -1
#
#
# Example Explanation
# Explanation 1:
#
#  In one operation we can swap A[0] with B3. So, A and becomes "0101".
# Explanation 2:
#
#  It is not possible to make both the strings equ