class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        count = 0
        pow = 1
        while True:
            if A // (5 ** pow) == 0:
                break
            else:
                zeros = A // (5 ** pow)
                count += zeros
        pow += 1

        return count
