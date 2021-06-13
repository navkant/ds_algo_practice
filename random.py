class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        a_dec = 0
        b_dec = 0

        for i in range(len(A) - 1, -1, -1):
            a_dec = a_dec + 2 ** int(A[i])

        for j in range(len(B) - 1, -1, -1):
            b_dec = b_dec + 2 ** int(B[i])

        result_dec = a_dec + b_dec
        result_binary = ""
        while True:
            if result_dec == 0:
                break
            else:
                remainder = result_dec % 2
                result_binary = resul_binary + str(remainder)
                result_dec = result_dec // 2

        return result_binary[::-1]
