class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        A = str(A)
        n = len(A)
        hash_map = {}

        for i in range(n):
            if int(A[i]) not in hash_map:
                hash_map[int(A[i])] = 1
            else:
                return 0
        print(hash_map)

        for i in range(n):
            product = int(A[i])
            for j in range(i + 1, n):
                product *= int(A[j])  # * int(A[j])
                print(product)
                if product not in hash_map:
                    hash_map[product] = 1
                else:
                    return 0

        return 1

if __name__ == '__main__':
    a = 123
    obj = Solution()
    ans = obj.colorful(a)
    print(f'ans is {ans}')