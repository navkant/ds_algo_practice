class Solution:
    def get_most_significant_bit(self, n):
        i = 0
        while 2 ** i <= n:
            i += 1
        return i
  
    def count_set_bits_till_padav(self, n):
        x = self.get_most_significant_bit(n) - 1
        return (x * (2**(x-1)))

    def count_most_significant_bit(self, n):
        i = self.get_most_significant_bit(n) - 1
        return n - (2**i) + 1
  
    def count_total_set_bits(self, n):
        a = self.count_set_bits_till_padav(n)
        b = self.count_most_significant_bit(n)
        return a + b

    def solve(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        x = self.count_set_bits_till_padav(n)
        y = self.count_most_significant_bit(n)
        msb = self.get_most_significant_bit(n)
        rest = n - (2**(msb-1))
        print('n: ', n)
        print('msb: ', msb)
        print('rest: ',rest)
        import pdb; pdb.set_trace()
        return x + y + self.solve(rest)
