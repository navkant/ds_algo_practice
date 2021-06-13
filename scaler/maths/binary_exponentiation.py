import sys
sys.setrecursionlimit(100000)


class Solution:
    def binary_exponentiation(self, a, b, p):
        x = a
        power = 1

        while True:
            if power * 2 >= b:
                break
            else:
                x = (x * x) % p
                power *= 2

        if power < b:
            x *= self.binary_exponentiation(a, b - power, p)

        return x % p

    def factorial(self, x):
        if x == 1:
            return 1

        return x * self.factorial(x-1)

    def solve(self, A, B):
        p = (10**9) + 7
        b_fact = self.factorial(B)
        print(f'fact {b_fact}')
        x = b_fact % (p-1)
        print(f'x {x}')

        a = self.binary_exponentiation(A, x, p)
        print(a)
        return a


if __name__ == '__main__':
    obj = Solution()
    ans = obj.solve(2, 27)
    print(f'ans is {ans}')
