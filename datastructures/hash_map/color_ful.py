class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        hash_map = dict()

        for i in A:
            if int(i) not in hash_map:
                hash_map[int(i)] = i
            else:
                return 0
        
        for i in range(len(A)):
            j = i + 1
            while j < len(A):
                sub_seq = ''
                sub_seq_product = 1
                for k in range(i, j+1):
                    # print(A[k], end=' ')
                    sub_seq = sub_seq + A[k]
                    sub_seq_product = sub_seq_product * int(A[k])
                if sub_seq_product not in hash_map:
                    hash_map[sub_seq_product] = sub_seq
                else:
                    return 0
                j += 1
                # print()
        return 1



if __name__ == "__main__":
    A = 99
    obj = Solution()
    ans = obj.colorful(A)
    print('ans is : ', ans)
