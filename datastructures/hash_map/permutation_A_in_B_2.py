import math

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer

    def __init__(self):
        primes = self.generate_n_primes(26) 
        self.char_prime_mapping = dict()
        primes_index = 0
        for i in range(97, 123):
            char = chr(i)
            self.char_prime_mapping[char] = primes[primes_index]
            primes_index += 1
        print(self.char_prime_mapping)

    def check_prime(self, num):
        root = int(math.sqrt(num))

        for i in range(root, num):
            if num % i == 0:
                return False
        return True

    def generate_n_primes(self, n):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        i = 29
        if n <= 10:
            return primes[:n]
        else:
            while True:
                if len(primes) == n:
                    break
                else:
                    i = i + 1
                    if self.check_prime(i):
                        primes.append(i)
                    else:
                        continue
        return primes

    def solve(self, A, B):
        string_product = 1
        for i in A:
            string_product = string_product * self.char_prime_mapping[i]
        print(string_product)

        i = 0
        count = 0
        substring_product = 1
        while True:
            if i >= len(B):
                break
            if i < len(A):
                substring_product = substring_product * self.char_prime_mapping[B[i]]
            else:
                substring_product  = substring_product * self.char_prime_mapping[B[i]]
                substring_product = substring_product // self.char_prime_mapping[B[i - len(A)]]
            print('substring_product: ', substring_product)
            if string_product == substring_product:
                count += 1
            i += 1
        return count


if __name__ == "__main__":
    A = "abc"
    A = A.lower()
    B = "abcbacabc"
    B = B.lower()
    obj = Solution()
    ans = obj.solve(A,B)
    print("ans is : ", ans)
