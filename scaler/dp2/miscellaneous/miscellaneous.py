class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def is_anagram(self, str1, str2):
        hash1 = {}
        for i in str1:
            if i not in hash1:
                hash1[i] = 1
            else:
                hash1[i] += 1
        hash2 = {}
        for i in str2:
            if i not in hash2:
                hash2[i] = 1
            else:
                hash2[i] += 1

        if hash1 == hash2:
            return True
        else:
            return False

    def is_scramble_recursive(self, A, B):
        print(f'A: {A} | B: {B}')
        if len(A) == len(B) == 1 and self.is_anagram(A, B):
            return 1

        if not self.is_anagram(A, B):
            return 0

        for i in range(1, len(A)):
            if self.is_scramble_recursive(A[:i], B[:i]) and self.is_scramble_recursive(A[i:], B[i:]):
                return 1
            if self.is_scramble_recursive(A[:i], B[len(B) - i:]) and self.is_scramble_recursive(A[i:], B[:len(B) - i]):
                return 1
        return 0

    def isScramble(self, A, B):
        ans = self.is_scramble_recursive(A, B)
        print(f'ans is {ans}')


if __name__ == '__main__':
    a = 'rgtae'
    b = 'great'
    obj = Solution()
    obj.isScramble(a, b)
